# FastAPI AWS Medieval Fair Gallery

This project is a medieval fair gallery created using FastAPI and AWS CDK. The gallery showcases images from an S3 bucket, giving it a medieval fair theme.

# Prerequisites
- Python (version 3.6 or higher)
- AWS account with CDK, S3, and IAM access
- AWS CLI and configured credentials
# Setup and Deployment
1. Clone the repository.

2. Install Python dependencies:

`pip install -r requirements.txt`

3. Set up AWS credentials using the AWS CLI:

`aws configure`

4. Install AWS CDK:

`npm install -g aws-cdk`

5. Deploy the AWS CDK stack:

`cdk deploy`

6. After deployment, the CDK will provide an output with the API endpoint URL.

7. Access the medieval fair gallery using the provided URL.

Enjoy the medieval fair experience with the amazing images from the S3 bucket!

_Note:_ Make sure to clean up the resources after use to avoid unnecessary costs. Run cdk destroy to delete the CDK stack and associated resources.