# from config import S3_BUCKET_NAME, S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from boto3 import client
import os


S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY")
S3_REGION = os.environ.get("S3_REGION")
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")

s3_client = client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION
)

# Create the Jinja2 templates object
templates = Jinja2Templates(directory="app/templates")


def get_objects_from_bucket(bucket_name: str) -> list:
    # List of objects in the S3 bucket
    response = s3_client.list_objects(Bucket=bucket_name)

    # Objects from the response
    objects = []

    if "Contents" in response:
        for obj in response["Contents"]:
            objects.append({
                "Key": obj["Key"],
                "ImageUrl": f"https://{bucket_name}.s3.amazonaws.com/{obj['Key']}"
            })

    return objects
