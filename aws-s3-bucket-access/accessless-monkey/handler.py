import boto3
s3_client = boto3.client('s3')

def get_access(event, context):
    obj = s3_client.get_object(Bucket='s3-bucket-access-dev-store', Key='happy-cat.jpg')
    print(obj)