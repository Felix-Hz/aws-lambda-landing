from config import S3_BUCKET_NAME, S3_ACCESS_KEY, S3_SECRET_KEY, S3_REGION
from app.api.content_grabber import get_objects_from_bucket
from app.api.upload import router as upload_router
from app.api.delete import router as delete_router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
import boto3

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION
)

app.include_router(upload_router)
app.include_router(delete_router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # get the objects from the S3 bucket
    objects = get_objects_from_bucket(S3_BUCKET_NAME)
    # rendering template
    return templates.TemplateResponse("index.html", {"request": request, "objects": objects})


# to run the server with uvicorn
if __name__ == "__main__":
    import uvicorn

    host = "0.0.0.0"
    port = 8000

    print(f"Server running at http://{host}:{port}/")
    uvicorn.run(app, host=host, port=port)
