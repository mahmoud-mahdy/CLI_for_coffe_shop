import os
from dotenv import load_dotenv
import logging
import shutil
from datetime import timedelta

import pyarrow.csv as pv
import pyarrow.parquet as pq

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

load_dotenv()

BUCKET_NAME = os.environ.get("BUCKET_NAME")
URL = 'https://files.grouplens.org/datasets/movielens/ml-latest.zip'
file_name = 'ml-latest.zip'


def format_to_parquet(dir):
    os.makedirs(f'{dir}/pq', exist_ok=True)
    os.makedirs(f'{dir}/csv', exist_ok=True)    
    
    for file in os.listdir(dir):
        if file.endswith('.csv'):
            shutil.move(f'{dir}/{file}', f'{dir}/csv/{file}')
            table = pv.read_csv(f'{dir}/csv/{file}')
            pq.write_table(table, f'{dir}/pq/{file}'.replace('.csv','.parquet'))
            print(f"created parquet for {file}")
    print("all csv files moved to csv folder")
    print("All Done")


default_args = {'owner': 'airflow',
        'start_date': days_ago(1),
        'depends_on_past': False,
        'retries': 0,
        'max_active_runs':1
        }


with DAG(dag_id='download_dataset_and_upload_to_gsc_dag',
        schedule_interval="@monthly",
        default_args=default_args,
) as dag:


# This is a BashOperator task that downloads the movielens dataset latest full version
    download_dataset_task = BashOperator(
        task_id="download_dataset",
        execution_timeout=timedelta(minutes=5),
        # The `-sSL` options are used to download the file in silent mode and follow any redirects.
        bash_command=f'curl -sSL {URL} > /opt/airflow/files/{file_name}; echo "Downloaded {file_name}";',
    )
    
    
    unzip_dataset_task = BashOperator(
        task_id="unzip_dataset",
        bash_command=f'unzip -o /opt/airflow/files/{file_name} -d /opt/airflow/files; rm /opt/airflow/files/{file_name}; echo "Unzipped {file_name}";',
        depends_on_past=True,
        execution_timeout=timedelta(minutes=2),
    )
    
    
    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet",
        depends_on_past=True,
        execution_timeout=timedelta(minutes=2),
        python_callable=format_to_parquet,
        op_kwargs={
            'dir': f'/opt/airflow/files/ml-latest',
        },
    )
    
    # upload pq files to GCS
    upload_tasks = []
    for file in os.listdir('/opt/airflow/files/ml-latest/pq'):
        if file.endswith('.parquet'):
            src = f'/opt/airflow/files/ml-latest/pq/{file}'
            if os.path.exists(src):
                upload_to_gsc_task  = LocalFilesystemToGCSOperator(
                task_id=f'upload_{file}_to_gcs',
                depends_on_past=True,
                execution_timeout=timedelta(minutes=5),
                src=src,
                dst=f'pq/{file}',
                bucket=BUCKET_NAME,
                gcp_conn_id='gcloud',
                )
                upload_tasks.append(upload_to_gsc_task)
        else:
            logging.warning(f'File {src} not found. Skipping upload.')
            continue
        
    download_dataset_task >> unzip_dataset_task >> format_to_parquet_task >> upload_tasks
    