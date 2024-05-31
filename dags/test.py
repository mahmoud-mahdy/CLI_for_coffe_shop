from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['your@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print_hello():
    print("Hello, Airflow!")

dag = DAG(
    'hello_airflow',
    default_args=default_args,
    description='A simple DAG to print hello',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 5, 30),
)

with dag:
    task_hello = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )
