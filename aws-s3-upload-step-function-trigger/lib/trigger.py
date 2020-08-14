import os
import json
import boto3

my_state_machine_arn = os.environ['MY_STATE_MACHINE_ARN']
client = boto3.client('stepfunctions')


def handler(event, context):
    print(event)
    for record in event['Records']:
        response = client.start_execution(
            stateMachineArn=my_state_machine_arn,
            input=json.dumps(record['s3'])
        )
