from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}
@dag(dag_id='our_first_dag_python_operator_v19',
     default_args=default_args,
     description='This is our first dag that we write',
     start_date=datetime(2025, 4, 29, 2),
     schedule_interval='@daily')
def hello_world_etl():
    @task
    def get_name():
        return "Jerry"
    @task()
    def get_age():
        return 30
    @task()
    def greet(name, age):
        print(f"Hello {name}, you are {age} years old")
    name = get_name()
    age = get_age()
    greet(name=name, age=age)
greet_dag = hello_world_etl()    
