from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
with DAG(
    "dvc_repro_daily",
    default_args=default_args,
    description="Run DVC repro command daily with --force option",
    schedule_interval="0 0 * * *",  # Daily at midnight
    start_date=datetime(2024, 10, 27),
    catchup=False,
) as dag:
    # Task to run the `dvc repro --force` command
    run_dvc_repro = BashOperator(
        task_id="run_dvc_repro",
        bash_command="dvc repro --force",
    )

    run_dvc_repro
