from __future__ import annotations

import os
from datetime import datetime
from airflow import DAG, macros
from airflow.operators.bash import BashOperator

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "Weather Test Data Pipeline"


with DAG(
    dag_id="Generate-Weather-Test-Data",
    start_date=datetime(2023, 7, 2),
    schedule_interval=None,
    catchup=False,
    tags=["battery-dev"],
) as dag:
    submit_job = BashOperator(
        task_id="generate_weather_test_data",
        bash_command='python /usr/local/airflow/scripts/genarate_mock_weather_events.py')


submit_job