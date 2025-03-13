# История изменений | Changelog

## Лабораторная работа 2: Airflow + Spark

### Добавлено | Added
- Интеграция Apache Spark с Airflow для выполнения Spark-задач. | Integrated Apache Spark with Airflow to execute Spark jobs.
- Добавлены сервисы `spark-master` и `spark-worker` в `docker-compose.yml`. | Added `spark-master` and `spark-worker` services to `docker-compose.yml`.
- Создан новый DAG `spark_dag.py` для отправки Spark-задачи с использованием `SparkSubmitOperator`. | Created a new DAG `spark_dag.py` to submit a Spark job using `SparkSubmitOperator`.
- Создана Spark-задача `task.py`, выполняющая простое преобразование данных. | Created a Spark job `task.py` that performs a simple data transformation.
- Добавлены необходимые зависимости в `Dockerfile`, включая `apache-airflow-providers-apache-spark`, `procps` и `default-jre`. | Added necessary dependencies to the `Dockerfile`, including `apache-airflow-providers-apache-spark`, `procps` and `default-jre`.

### Обновлено | Updated
- Обновлен `docker-compose.yml` для включения сервисов Spark и использования `SequentialExecutor`. | Updated `docker-compose.yml` to include Spark services and use `SequentialExecutor`.
- Обновлен README.md с инструкциями по настройке и запуску интеграции Spark. | Updated README.md with instructions on how to set up and run the Spark integration.

### Зависимости | Dependencies
- Добавлен `apache-airflow-providers-apache-spark` в список необходимых пакетов Python. | Added `apache-airflow-providers-apache-spark` to the list of required Python packages.