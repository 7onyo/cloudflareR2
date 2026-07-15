import boto3
import dotenv
import os
import sys
from botocore.exceptions import ClientError

dotenv.load_dotenv()
file_to_upload = os.getenv('FILE_TO_UPLOAD')
bucket_name = os.getenv('BUCKET_NAME')

if not file_to_upload or not bucket_name:
    print("Error: FILE_TO_UPLOAD and BUCKET_NAME must be set in .env")
    sys.exit(1)


s3 = boto3.client(
    's3',
    endpoint_url=os.getenv('R2_ENDPOINT_URL'),
    aws_access_key_id=os.getenv('R2_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('R2_SECRET_ACCESS_KEY'),
    region_name='auto' 
)

try:
    object_name = os.path.basename(file_to_upload)
    s3.upload_file(file_to_upload, bucket_name, object_name)
    print("Upload successful!")
except ClientError as e:
    print(f"Error: {e}")