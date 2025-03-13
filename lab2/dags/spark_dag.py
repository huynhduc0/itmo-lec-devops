from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('spark_example',
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    submit_job = SparkSubmitOperator(
        task_id='submit_my_spark_job',
        application='/opt/airflow/spark/task.py',
        conn_id='spark_local',
        name='Spark Job'
    )