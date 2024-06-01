# dag to upload file to gsc bucket

from airflow import DAG
from datetime import datetime

default_args = {    
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now() - datetime.timedelta(days=1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}