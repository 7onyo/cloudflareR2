import boto3
import dotenv
import os
from botocore.exceptions import ClientError

dotenv.load_dotenv()

s3 = boto3.client(
    's3',
    endpoint_url=os.getenv('R2_ENDPOINT_URL'),
    aws_access_key_id=os.getenv('R2_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('R2_SECRET_ACCESS_KEY'),
    region_name='auto' 
)

try:
    s3.upload_file('./CV.pdf', 'myresume', 'CV.pdf')
    print("Upload successful!")
except ClientError as e:
    print(f"Error: {e}")