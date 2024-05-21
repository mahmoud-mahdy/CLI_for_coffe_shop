from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'upload_to_gcs',
    default_args=default_args,
    description='DAG to upload a file to GCS',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

upload_task = LocalFilesystemToGCSOperator(
    task_id='upload_file_to_gcs',
    src='test.py',  # Change this to the path of your local file
    dst='test.py',  # Change this to the desired destination file name
    bucket='data_lake_spark',  # Change this to your GCS bucket name
    dag=dag
)

# If there are more tasks, they would typically be set up like this:
# task1 >> upload_task >> task3



