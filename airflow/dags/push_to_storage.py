from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from scripts.push_to_storage import push_to_storage

# Define the DAG
# Define the default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Initialize the DAG
with DAG(
    "upload_dataset_to_s3",
    default_args=default_args,
    description="A DAG to upload dataset to S3",
    schedule_interval="0 0 * * *",  # Runs daily at midnight
    start_date=datetime(2024, 10, 29),
    catchup=False,
) as dag:
    # Define the PythonOperator to execute the function
    upload_task = PythonOperator(
        task_id="upload_to_s3",
        python_callable=push_to_storage,
    )

    upload_task
