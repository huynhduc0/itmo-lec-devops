from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello from Airflow!")

def print_world():
    print("World from Airflow!")

default_args = {
    'start_date': datetime(2024, 3, 1),
    'catchup': False
}

with DAG('example_dag',
         default_args=default_args,
         schedule_interval='@daily') as dag:

    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

    task2 = PythonOperator(
        task_id='print_world',
        python_callable=print_world
    )

    task1 >> task2
