# get data from link to gcs
import os
import logging
import zipfile
from datetime import timedelta

import pyarrow.csv as pv
import pyarrow.parquet as pq

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

URL = 'https://files.grouplens.org/datasets/movielens/ml-latest.zip'
file_name = 'movielens-latest.zip'

def unzip_file(file_name, extract_to):
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(file_name)


def format_to_parquet(dir):
    os.makedirs(f'{dir}/pq', exist_ok=True)
    for file in os.listdir(dir):
        
        if file.endswith('.csv'):
            table = pv.read_csv(f'{dir}/{file}')
            pq.write_table(table, f'{dir}/pq/{file}'.replace('.csv','.parquet'))



default_args = {'owner': 'airflow',
        'start_date': days_ago(1),
        'depends_on_past': False,
        'retries': 0,
        'max_active_runs':1
        }


with DAG(dag_id='data_to_gcs_dag',
        schedule_interval="@daily",
        default_args=default_args,
) as dag:


    
    download_dataset_task = BashOperator(
        task_id="download_dataset",
        execution_timeout=timedelta(minutes=2),
        bash_command=f'curl -sSL {URL} > /opt/airflow/files/{file_name}; echo "Downloaded {file_name}";',
    )
    
    
    unzip_dataset_task = PythonOperator(
        task_id="unzip_dataset",
        execution_timeout=timedelta(seconds=60),
        python_callable=unzip_file,
        op_kwargs={
            'file_name': f'/opt/airflow/files/{file_name}',
            'extract_to': f'/opt/airflow/files/',
        }
        
    )
    
    
    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet",
        execution_timeout=timedelta(seconds=60),
        python_callable=format_to_parquet,
        op_kwargs={
            'dir': f'/opt/airflow/files/ml-latest',
        },
    )
    
    
    download_dataset_task >> unzip_dataset_task >> format_to_parquet_task