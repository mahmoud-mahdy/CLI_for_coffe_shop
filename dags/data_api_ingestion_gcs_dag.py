import os
from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

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

# Print out the current directory
print_dir_task = BashOperator(
    task_id="print_dir",
    bash_command="ls -la",
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