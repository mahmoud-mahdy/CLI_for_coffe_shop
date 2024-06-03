
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from airflow.utils.dates import days_ago


DATASET_NAME = 'MovieLens'
BUCKET_NAME = 'data_lake_231'

def test():
    

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
    

    # move pq files from gcs to bigquery
    transfer_files_to_bigquery  = GCSToBigQueryOperator(
        task_id='transfer_files_to_bigquery',
        bucket=BUCKET_NAME,
        source_objects="{{ task_instance.xcom_pull(task_ids='list_files') }}",
        destination_project_dataset_table=f'{DATASET_NAME}.dataset',
        source_format="PARQUET",
        gcp_conn_id='gcloud',
        autodetect=True
    )
    
    python_task = PythonOperator(
        task_id='python_task',
        python_callable=
    )
        
    list_files >>transfer_files_to_bigquery
