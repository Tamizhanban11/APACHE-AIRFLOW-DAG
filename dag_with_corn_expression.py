from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='dag_with_corn_expression_v09',
    default_args=default_args,
    start_date=datetime(2023, 10, 1),
    schedule_interval='0 0 * * *',  # This is a cron expression for daily
) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "I am a data enthusiast"'
    )
