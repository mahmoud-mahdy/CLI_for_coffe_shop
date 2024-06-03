
from airflow import DAG
from airflow.providers.google.cloud.operators.gcs import GCSToBigQueryOperator
from airflow.utils.dates import days_ago


DATASET_NAME = 'MovieLens'


default_args = {'owner': 'airflow',
        'start_date': days_ago(1),
        'retries': 0,
        'max_active_runs':1
        }

with DAG(dag_id='download_dataset_dag',
        schedule_interval="@daily",
        default_args=default_args,
) as dag:

    # upload pq files from gcs to bigquery
    for file in os.listdir('/opt/airflow/files/')
    upload_dataset_task = GCSToBigQueryOperator(
        task_id="upload_dataset",
        bucket="zoomcamp-bucket",
        source_objects=[f'/opt/airflow/files/ml-latest/pq/{file}'],
        destination_project_dataset_table=f"{DATASET_NAME}.ratings",