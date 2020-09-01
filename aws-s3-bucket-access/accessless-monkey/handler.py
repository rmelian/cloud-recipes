import os
import boto3
s3_client = boto3.client('s3')
BUCKET = os.environ['BUCKET']

def get_access(event, context):
    obj = s3_client.get_object(Bucket=BUCKET, Key='photo.jpg')
    print(obj)

