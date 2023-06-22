from config import S3_BUCKET_NAME, S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION
from app.api.content_grabber import get_objects_from_bucket
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
import botocore.exceptions
import boto3
import os

# S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
# S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY")
# S3_REGION = os.environ.get("S3_REGION")
# S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.delete("/delete/{key}")
async def delete_object(request: Request, key: str):
    try:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=S3_ACCESS_KEY,
            aws_secret_access_key=S3_SECRET_KEY,
            region_name=S3_REGION
        )
        
        # Delete the object from the S3 bucket
        s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=key)

        # flags for the html
        context = {
            "message": f"Object with key '{key}' deleted successfully",
            "success": True  
        }

        objects = get_objects_from_bucket(S3_BUCKET_NAME)

        return templates.TemplateResponse("index.html", {"request": request, "objects": objects, **context})
    except botocore.exceptions.ClientError as e:

        # flags for the html
        context = {
            "message": f"Error deleting image to S3. Due to Error: {e}",
            "success": False 
        }

        objects = get_objects_from_bucket(S3_BUCKET_NAME)

        return templates.TemplateResponse("index.html", {"request": request, "objects": objects, **context})
