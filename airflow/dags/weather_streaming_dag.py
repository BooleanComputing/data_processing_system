from __future__ import annotations

import os
from datetime import datetime
from airflow import DAG, macros
from airflow.operators.bash import BashOperator
from datetime import datetime as dt, timedelta

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "Weather Streaming Pipeline"


with DAG(
    dag_id="Weather-Streaming",
    start_date=datetime(2023, 7, 3),
    schedule_interval=timedelta(minutes=25),
    catchup=False,
    tags=["battery-dev"],
) as dag:
    submit_job = BashOperator(
        task_id="spark_submit_image_streaming",
        bash_command='${AIRFLOW_HOME}/scripts/spark/bin/spark-submit --jars ${AIRFLOW_HOME}/scripts/spark_jars/commons-pool2-2.11.1.jar,${AIRFLOW_HOME}/scripts/spark_jars/spark-sql-kafka-0-10_2.12-3.4.0.jar,'
                     '${AIRFLOW_HOME}/scripts/spark_jars/kafka-clients-3.4.0.jar,${AIRFLOW_HOME}/scripts/spark_jars/spark-token-provider-kafka-0-10_2.12-3.4.0.jar --master spark://spark:7077 '
                     '--name image-streaming ${AIRFLOW_HOME}/scripts/weather_streaming.py kafka-1:9092  weather_data weather_data_avg {{ execution_date }}')


submit_job