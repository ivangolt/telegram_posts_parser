import logging
import subprocess
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Set up logging
logger = logging.getLogger("airflow.task")


def run_upload_dataset_to_s3():
    logger.info("Starting upload_dataset_to_s3 task")
    try:
        subprocess.run(
            ["python", "C:/dev/telegram_posts_parser/scripts/push_to_storage.py"],
            check=True,
        )
        logger.info("Successfully completed upload_dataset_to_s3 task")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error in upload_dataset_to_s3 task: {e}")


# Define the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 10, 28),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "daily_data_pipeline",
    default_args=default_args,
    description="Daily pipeline to load, transform, and upload dataset",
    schedule_interval="0 0 * * *",  # Runs every day at 00:00
    catchup=False,
) as dag:
    # Define tasks

    upload_dataset_task = PythonOperator(
        task_id="upload_dataset_to_s3", python_callable=run_upload_dataset_to_s3
    )

    upload_dataset_task
