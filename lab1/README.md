# Лабораторная работа 1: Airflow + Docker Compose
# Lab 1: Airflow + Docker Compose

##  Оглавление | Table of Contents
- [Установка | Installation](#-установка--installation)
- [Запуск | Running](#-запуск--running)
- [Скриншоты | Screenshots](#-скриншоты--screenshots)
- [Описание проекта | Project Description](#-описание-проекта--project-description)

---

## Установка | Installation
1.  Убедитесь, что установлены **Docker** и **Docker Compose**.  
    Make sure **Docker** and **Docker Compose** are installed.
2.  Клонируйте репозиторий | Clone the repository:

    ```sh
    git clone https://gitlab.com/huynhduc0/itmo-lec-devops.git
    cd itmo-lec-devops/lab1
    ```
3.  Постройте Docker-образ | Build the Docker image:

    ```sh
    docker-compose build
    ```

## Запуск | Running

1.  Запустите Airflow с помощью Docker Compose | Start Airflow with Docker Compose:

    ```sh
    docker-compose up -d
    ```

2.  Проверьте, запущены ли контейнеры | Check running containers:

    ```sh
    docker ps
    ```

3.  Перейдите в веб-интерфейс Airflow | Open Airflow UI:

    [http://localhost:8080/](http://localhost:8080/)

    Логин | Login: `airflow`  
    Пароль | Password: `airflow`

## Скриншоты | Screenshots

1.  Запущенные контейнеры | Running Containers
    ![docker](/lab1/img/docker-ps.png)

2.  Список DAG-ов | DAGs List
    ![dags](/lab1/img/dags.png)

3.  Информация о DAG | DAG Info
    ![dag](/lab1/img/dag_info.png)

## Описание проекта | Project Description
Этот проект разворачивает Apache Airflow с помощью Docker Compose.  
This project deploys Apache Airflow using Docker Compose.

### Структура проекта | Project Structure

```bash
airflow-lab/
│── dags/                  # Папка с DAG-ами
│   └── test_dag.py      # Пример DAG
│── img/                # Папка с изображениями для документации
│── Dockerfile             # Конфигурация Docker-образа
│── docker-compose.yml     # Конфигурация Docker Compose
│── README.md              # Этот файл
```

Чыонг Хюинь Дык (Truong Huynh Duc)