
import os

from airflow.models import TaskInstance
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from airflow.utils.dates import days_ago


PROJECT_ID = 'cryptic-smile-413720'
DATASET_NAME = 'MovieLens'
BUCKET_NAME = 'data_lake_231'

def transfer_files_to_bigquery(**context):
    # Initialize the operator
    list_files_output = context['ti'].xcom_pull(task_ids='list_files')
    for file in list_files_output:
        file = file.replace("pq/", "")
    
        transfer_files_to_bigquery  = GCSToBigQueryOperator(
            task_id='transfer_files_to_bigquery',
            bucket=BUCKET_NAME,
            source_objects="pq/*.parquet",
            destination_project_dataset_table=f'{DATASET_NAME}.{DATASET_NAME}.{file}',
            source_format="PARQUET",
            gcp_conn_id='gcloud',
            autodetect=True
        )
        
    

default_args = {'owner': 'airflow',
        'start_date': days_ago(1),
        'retries': 0,
        'max_active_runs':1
        }


with DAG(dag_id='gsc_to_bg_dag',
        schedule_interval="@daily",
        default_args=default_args,
) as dag:

    # read files in gsc
    list_files = GCSListObjectsOperator(
        task_id='list_files',
        bucket=BUCKET_NAME,
        prefix='pq/',
        gcp_conn_id='gcloud'
    )

    
    run_transfer = PythonOperator(
    task_id='move_pq_files_to_bigquery',
    python_callable=transfer_files_to_bigquery,
    )
        
    list_files >> run_transfer
