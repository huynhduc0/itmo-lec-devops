from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 3, 1),
    'catchup': False
}

with DAG('spark_dag',
         default_args=default_args,
         schedule_interval=None,
         tags=['spark']) as dag:

    spark_job = SparkSubmitOperator(
        task_id='run_spark_job',
        application='local:///opt/airflow/dags/submit.py',
        conn_id='spark_local',
        verbose=True,
        conf={
            "spark.driver.memory": "4g",
            "spark.executor.memory": "4g",
            "spark.network.timeout": "1000s",
            "spark.rpc.message.maxSize": "512",
            "spark.driver.maxResultSize": "2g",
            "spark.sql.broadcastTimeout": "3000",
            "spark.executor.heartbeatInterval": "100s",
            "spark.shuffle.io.maxRetries": "10",
            "spark.shuffle.io.retryWait": "10s",
            "spark.core.connection.ack.wait.timeout": "600s"
        },
        dag=dag
    )

    spark_job
