#test again 4000
import json
import boto3
import logging
import re
import csv
import pandas as pd
import datetime
import time
import  io
import sys
import psycopg2
client=boto3.client('s3')
def lambda_handler(event, context):
   
    # #getting credentails from parameter store to connect to redshift
    redshift_login_details=redshift_credentials()
    conn=setup_db_connection(redshift_login_details) #passing parameters to establish connection with redshift
    tables_creation(conn)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    data=open_project_csv(object_key,bucket_name)
    print('data before transformation')
    print(format_dataframe_summary(pd.DataFrame(data)))
    #perform transformation
    data=data_cleaning(data)
    print('data after transformation')
    print(format_dataframe_summary(pd.DataFrame(data)))

    load_customers(data,conn) # loading customers to database
    load_products(data,conn)
    load_orders(data,conn)
    print('Done loading file into redshift')
    
    return {
            'statusCode': 200,
            'body': sys.version
        }


##############################################
############ Extraction  #################
def open_project_csv(filename,bucketname):
    
    try:
        response = client.get_object(Bucket=bucketname, Key=filename)
        csv_content = response['Body'].read().decode('utf-8')
        
        # Parse CSV content line by line
        orders_list = []
        fieldnames=['date', 'location', 'name', 'order', 'price', 'payment_method','Account_Number']
        csv_reader = csv.DictReader(io.StringIO(csv_content), fieldnames=fieldnames)
        orders_list = [row for row in csv_reader]
        return orders_list
    except Exception as e:
        print(e)
##############################################
############ Loading Section  #################
def tables_creation(conn):
    print('making tables')
    cursor=conn.cursor()
    cursor.execute('''
                  create table IF NOT EXISTS customers(
        customer_id INT IDENTITY(1,1) PRIMARY KEY,
        location VARCHAR(255) NOT NULL
        );''')
    conn.commit()
    cursor.execute('''
                  create table IF NOT EXISTS orders(
            order_id INT IDENTITY(1,1) PRIMARY KEY,
            date DATE  NOT NULL,
            customer_id integer not null,
            payment_method varchar(20) default 'CARD',
            total_price numeric not null,
            foreign key(customer_id) references customers(customer_id)
            );''')
    conn.commit()
    cursor.execute('''
                  create table IF NOT EXISTS products(
            product_id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            total_price numeric not null
            );''')
    conn.commit()
    cursor.execute('''
                  create table IF NOT EXISTS order_items(
            item_id INT IDENTITY(1,1) PRIMARY KEY,
            order_id int,
            product_id int,
            quantity varchar(20) not null,
            foreign key(product_id) references products(product_id),
            foreign key(order_id) references orders(order_id)
            );''')
    conn.commit()


            
def load_customers(data,connection):
    cursor = connection.cursor()
    print('customer data')
    print(data)
    # Extract locations from the data list
    locations = [customer['location'] for customer in data]
   
    try:
        # Use executemany to insert multiple rows in a single query
        cursor.executemany(
            '''INSERT INTO data_xcelerator_cafe_db.public.customers(location) VALUES (%s)''',
            [(location,) for location in locations]
        )
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

            
        
def load_orders(data,connection):
    
    cursor=connection.cursor()
    cursor.execute('SELECT MAX(customer_id) FROM data_xcelerator_cafe_db.public.customers')
    customer_id = cursor.fetchone()[0] or 1
    # Define the format of your date string
    date_format = '%d/%m/%Y %H:%M'
    
    for index,order in enumerate(data,start=customer_id):
        
        date_time_object = datetime.datetime.strptime(order['date'], date_format)
        # loading data to orders table
        cursor.execute(''' insert into data_xcelerator_cafe_db.public.orders (date,customer_id,payment_method,total_price) values (%s,%s,%s,%s)
                      ''',[date_time_object,index,order['payment_method'],order['price']])
        connection.commit()
        # loading data to order_items table
        products=products_preprocessing([order])
        for product in products:
            cursor.execute('select product_id from data_xcelerator_cafe_db.public.products where name=(%s)',[product['name']]) # getting product id products table
            product_id=cursor.fetchone()[0] 
            df=pd.DataFrame(products)
            count_value=(df['name'] == product['name']).sum() # counting product quanity form given order
            cursor.execute('''select order_id  from data_xcelerator_cafe_db.public.orders ORDER BY order_id DESC LIMIT 1;''') # getting the order id for latest order
            order_id=cursor.fetchone()[0] 
            # storing data into order item table
            cursor.execute('''insert into data_xcelerator_cafe_db.public.order_items (order_id,product_id,quantity) values(%s,%s,%s)''',(int(order_id),int(product_id),int(count_value)))
            connection.commit()
            

def load_products(data, connection):
  
    data = products_preprocessing(data)
    df = pd.DataFrame(data)
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['name', 'price'])
    
    # Convert DataFrame to list of tuples
    products = [tuple(row) for row in df[['name', 'price']].to_records(index=False)]
    
    cursor = connection.cursor()

    try:
        # Batch insertion using executemany
        cursor.executemany('''INSERT INTO data_xcelerator_cafe_db.public.products (name, total_price) VALUES (%s, %s)''', products)
        connection.commit()
        print('Products loaded successfully')
    except Exception as e:
        print(e)
    finally:
        cursor.close()


##############################################
############ Transformation  #################
def data_cleaning(data):
    df = pd.DataFrame(data)
    # Drop rows with any null or missing values
    df.dropna(inplace=True)
    # Convert DataFrame back to list of dictionaries
    data = df.to_dict(orient='records')
    return data
def products_preprocessing(data):
    """
    1): converted "Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45"
    to ['Regular', 'Flavoured', 'iced', 'latte', '-', 'Hazelnut', '-', '2.75,'], ['Large', 'Latte', '-', '2.45']
    2): converted ['Regular', 'Flavoured', 'iced', 'latte', '-', 'Hazelnut', '-', '2.75,'], ['Large', 'Latte', '-', '2.45']
    to [{'name': ' Regular Flavoured iced latte Hazelnut', 'price': 2.75}, {'name': ' Large Latte', 'price': 2.45}]
    returns [{'name': ' Regular Flavoured iced latte Hazelnut', 'price': 2.75}, {'name': ' Large Latte', 'price': 2.45}]
    """
    try:
        
        list_order=[order['order'].split() for order in data]
        splited_products=[]
        pattern = re.compile(r'^\d+\.\d+$')
        for order in list_order:
            for _,value in enumerate(order):
                if pattern.match(value.rstrip(',')): # matching the name to pattern
                    splited_products.append(order[:order.index(value)+1]) # appending the order to
                    order=order[order.index(value)+1:]
    except Exception as e:
        print(e)
    products=[]
    for product in splited_products:
        temp_dict={'name':'',
            'price':0}
        for name in product:
            try:
                if name.isalpha():
                    temp_dict['name']=temp_dict['name']+" "+name
                else:
                    if name=='-':
                        continue
                    else:
                        temp_dict['price']=float(name.rstrip(','))
            except Exception as e:
                print(e)
        products.append(temp_dict)
    
            
    return products

###################################################
############ RedShift Connection  #################
def redshift_credentials():
    
    # ssm_client = boto3.client('ssm', region_name='eu-west-1')
    ssm_client = boto3.client('ssm', region_name='eu-west-1')
    # Get the SSM Param from AWS and turn it into JSON
    # Don't log the password!
    parameter_details = ssm_client.get_parameter(Name='data_xcelerator_redshift_settings')
    redshift_details = json.loads(parameter_details['Parameter']['Value'])
    print(redshift_details)
    return redshift_details
    
def setup_db_connection(redshift_login_details):
    print('connect')
    try:
        connection = psycopg2.connect(
            host='10.0.0.4',
            database=redshift_login_details['database-name'],
            user=redshift_login_details['user'],
            port=5439,
            password=redshift_login_details['password'],
        )
        return connection
    except Exception as e:
        print(e)
    print('end of conecton')

def format_dataframe_summary(df):
    # Null values in each column
    null_values = df.isnull().sum().to_dict()

    # Missing values in each column (NaN, None, etc.)
    missing_values = df.isna().sum().to_dict()

    # Summary of data including count, mean, std, min, 25%, 50%, 75%, max
    data_summary = df.describe(include='all').to_string()

    # Data types of each column
    data_types = df.dtypes.to_dict()

    # Count of unique values in each column
    unique_values = {col: df[col].nunique() for col in df.columns}

    summary = {
        "Null Values in Each Column": null_values,
        "Missing Values in Each Column": missing_values,
        "Data Summary": data_summary,
        "Data Types": data_types,
        "Unique Values Count": unique_values
    }

    return summary

# Example usage
# df = pd.read_csv('your_dataset.csv')  # Load your dataset here
# summary = format_dataframe_summary(df)
# print(summary)
#new comment
# added test 02