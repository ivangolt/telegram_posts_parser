import logging

import boto3
import click
from botocore.client import Config

from airflow.hooks.base import BaseHook

logging.basicConfig(level=logging.INFO)

aws_conn = BaseHook.get_connection("aws_default")


# Upload the file
@click.command()
def push_to_storage():
    ENDPOINT_URL = "https://s3.cloud.ru"
    BUCKET_NAME = "bucket-be6cd7"
    AWS_ACCESS_KEY_ID = (
        "7360e237-d11f-4989-add5-16dbb5ff0703:e877c694f46e64740b3fe6a50dcdb739"
    )
    AWS_SECRET_ACCESS_KEY = "1d9e5743c2dda58d039a45c1d3b9113f"

    #    File to upload
    FILE_PATH = "data/posts_prepared.csv"
    OBJECT_NAME = "posts_prepared.csv"  # The name of the file in the bucket

    # Initialize the S3 client
    s3_client = boto3.client(
        "s3",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=aws_conn.login,
        aws_secret_access_key=aws_conn.password,
        config=Config(signature_version="s3v4"),
    )
    logging.info("Initialize S3 client")

    try:
        logging.info("Starting uploading file...")
        s3_client.upload_file(FILE_PATH, BUCKET_NAME, OBJECT_NAME)
        logging.info(
            f"Successfully uploaded {FILE_PATH} to {BUCKET_NAME}/{OBJECT_NAME}"
        )
    except Exception as e:
        print(f"Failed to upload {FILE_PATH} to {BUCKET_NAME}/{OBJECT_NAME}: {e}")


if __name__ == "__main__":
    push_to_storage()
