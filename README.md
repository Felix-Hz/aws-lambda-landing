# FastAPI Landing Page with AWS (EC2, Lambda, S3) Integration

This project showcases a landing page developed using FastAPI in Python. The landing page allows users to upload images, and the project integrates with AWS EC2 and Lambda to display the names and details of the newly uploaded images from an S3 bucket.

## Prerequisites

Python (version 3.6 or higher)
AWS account with EC2, S3, and Lambda access
AWS CLI and configured credentials
## Setup and Deployment

1. Clone the repository.
2. Install Python dependencies:

`pip install -r requirements.txt`

3. Set up AWS credentials using the AWS CLI:

`aws configure`

4. Create an EC2 instance in your AWS account.

5. SSH into the EC2 instance and clone the repository.
6. Configure the EC2 instance with necessary dependencies.
7. Set up an S3 bucket and Lambda function.
8. Update the FastAPI application's configuration file with AWS credentials and bucket details.
9. Start the FastAPI application:

`uvicorn main:app --host 0.0.0.0 --port 8000`

10. Access the landing page using the EC2 instance's public IP address or DNS name.