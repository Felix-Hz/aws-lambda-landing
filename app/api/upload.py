# from config import S3_BUCKET_NAME, S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION
from app.api.content_grabber import get_objects_from_bucket
from fastapi import APIRouter, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
import botocore
import boto3
import os

router = APIRouter()

S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY")
S3_REGION = os.environ.get("S3_REGION")
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")


s3_client = boto3.client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION
)

templates = Jinja2Templates(directory="app/templates")


@router.post("/upload")
async def upload_file(request: Request, image: UploadFile = File(...)):
    try:
        # temporary file
        with open(image.filename, "wb") as temp_file:
            temp_file.write(await image.read())

        # to S3
        s3_client.upload_file(image.filename, S3_BUCKET_NAME, image.filename)

        # delete temp file
        os.remove(image.filename)

        # flags for the html
        context = {
            "message": "Image uploaded successfully",
            "success": True  
        }

        objects = get_objects_from_bucket(S3_BUCKET_NAME)

        return templates.TemplateResponse("index.html", {"request": request, "objects": objects, **context})
    except botocore.exceptions.ClientError as e:

        # flags for the html
        context = {
            "message": f"Error uploading image to S3. Due to Error: {e}",
            "success": False 
        }

        objects = get_objects_from_bucket(S3_BUCKET_NAME)

        return templates.TemplateResponse("index.html", {"request": request, "objects": objects, **context})
