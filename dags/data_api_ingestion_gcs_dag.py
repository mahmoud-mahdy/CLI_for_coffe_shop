import csv
import json
from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from datetime import datetime
from airflow.operators.python import PythonOperator
import requests

with open('ebay_config.json', 'r') as file:
    credentials = json.load(file)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

dag = DAG(
    'upload_to_gcs',
    default_args=default_args,
    description='A DAG to upload a file to GCS',
    schedule_interval=None, 
)

def fetch_iphone_14_list():
    headers = {
    'Authorization': f"Bearer {credentials['token']}",
    'Content-Type': 'application/json',
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'  # Adjust this depending on the marketplace you're targeting
}
    # Construct the API endpoint
    query = 'iphone 14'  # Search query
    limit = 100  #? ebay only allow maximum of 200
    url = f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&limit={limit}' # item_summary/search only look for buy now items no auctions

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        dict = {}
        json_list = response.json()
        
        
        fieldnames=['itemId', 'title', 'price', 'shipping cost', 'seller', 'seller feedback Percentage', 'seller feedback Score', 'seller', 'condition', 'URL']
        with open('iphone_14_list.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
                       
        for item in json_list['itemSummaries']:
            dict['itemId'] = item['itemId']
            dict['title'] = item['title']
            dict['price'] = item['price']['value']
            dict['shipping cost'] = item['shippingOptions'][0]['shippingCost']['value']
            # dict['location'] = item['itemLocation']['postalCode']
            dict['seller'] = item['seller']['username']
            dict['seller feedback Percentage'] = item['seller']['feedbackPercentage']
            dict['seller feedback Score'] = item['seller']['feedbackScore']
            dict['seller'] = item['seller']['sellerAccountType']
            dict['condition'] = item['condition']
            dict['URL'] = item['itemWebUrl']
            
            with open('iphone_14_list.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=dict.keys())
                writer.writerow(dict)

        print(f"Successfully retrieved data: {response.status_code} - {response.text}")
    else:
        print(f"Failed to retrieve data: {response.status_code} - {response.text}")


print_dir_task = PythonOperator(
    task_id="fetch_data",
    python_callable=fetch_iphone_14_list,
    dag=dag
)

# List GCS objects
list_gcs_objects = GCSListObjectsOperator(
        task_id='list_gcs_objects',
        bucket='data_lake_231',
        gcp_conn_id='gcloud',
        dag=dag
    )

# Upload the file to GCS
upload_file = LocalFilesystemToGCSOperator(
    task_id="upload_file",
    src='files/iphone_14_list.csv',
    dst='iphone_14_list.csv',
    bucket='data_lake_231',
    gcp_conn_id='gcloud',
    dag=dag
    )

print_dir_task >> list_gcs_objects >> upload_file