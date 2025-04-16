from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet():
  print("Hello, this is our first Python operator task!")

with DAG(
  default_args=default_args,
  dag_id='our_first_dag_python_operator_v01',
  description='This is our first dag that we write',
  start_date=datetime(2025, 4, 29, 2),
  schedule_interval='@daily'
)as dag:
  task1 = PythonOperator(
    task_id='first_task',
    python_callable=greet
  )
  task1