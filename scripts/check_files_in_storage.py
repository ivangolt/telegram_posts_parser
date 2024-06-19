import boto3
from botocore.client import Config

ENDPOINT_URL = "https://s3.cloud.ru"

BUCKET_NAME = "bucket-be6cd7"


# Initialize the S3 client
s3_client = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id="7360e237-d11f-4989-add5-16dbb5ff0703:e877c694f46e64740b3fe6a50dcdb739",
    aws_secret_access_key="1d9e5743c2dda58d039a45c1d3b9113f",
    config=Config(signature_version="s3v4"),
)

# List the files in the bucket
try:
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
    if "Contents" in response:
        for obj in response["Contents"]:
            print(obj["Key"])
    else:
        print(f"No files found in bucket {BUCKET_NAME}")
except Exception as e:
    print(f"Failed to list files in bucket {BUCKET_NAME}: {e}")
