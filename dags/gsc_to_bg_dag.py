import os
from dotenv import load_dotenv

from airflow.providers.google.cloud.hooks.gcs import GCSHook
from google.cloud import storage
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator
from airflow.utils.dates import days_ago

load_dotenv()

PROJECT_ID = os.environ.get("PROJECT_ID")
DATASET_NAME = os.environ.get("DATASET_NAME")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
      

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
}


with DAG(
    dag_id="gcs_to_bq_dag",
    schedule_interval="@monthly",
    default_args=default_args,
    max_active_runs=1,
) as dag:
    
    
    gsc_to_bq_tasks = []
    gcs_hook = GCSHook(gcp_conn_id='gcloud')
    client = storage.Client(credentials=gcs_hook.get_credentials()) #!
    bucket = client.bucket(BUCKET_NAME)
    prefix = 'pq/'
    blobs = bucket.list_blobs(prefix=prefix)
    
    for blob in blobs:
        file_name = blob.name
        file_name = file_name.replace('pq/','')
        file_name = file_name.replace('.parquet','')
        
        bigquery_external_table_task = BigQueryCreateExternalTableOperator(
            task_id=f"bq_{file_name}_external_table_task",
            table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": DATASET_NAME,
                "tableId": f"{file_name}_external_table"
            },
            "externalDataConfiguration": {
                "autodetect": "True",
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET_NAME}/pq/{file_name}.parquet"]
            }},
            gcp_conn_id='gcloud'
        )
        gsc_to_bq_tasks.append(bigquery_external_table_task)
     
    gsc_to_bq_tasks