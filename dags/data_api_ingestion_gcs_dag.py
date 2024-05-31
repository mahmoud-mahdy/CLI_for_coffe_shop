from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'upload_to_gcs',
    default_args=default_args,
    description='A DAG to upload a file to GCS',
    schedule_interval=None, 
)

upload_file = LocalFilesystemToGCSOperator(
    task_id="upload_file",
    src='C:\\Users\\ellat\\OneDrive\\Desktop\\zoom_camp_data_engineer\\Zoom-camp-data-pipeline-project\\files\\iphone_14_list.csv',
    dst='iphone_14_list.csv',
    bucket='data_lake_231',
    gcp_conn_id='gcloud',
    dag=dag
    )

upload_file