FROM apache/airflow:slim-2.10.5-python3.8

WORKDIR /opt/airflow

USER root
RUN apt update && apt -y install procps default-jre

USER airflow
COPY ./dags/* ./dags/
COPY ./spark/* ./spark/

RUN pip3 install apache-airflow-providers-apache-spark psycopg2-binary
