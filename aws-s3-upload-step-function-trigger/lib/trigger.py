import os
import json
import boto3

my_state_machine_arn = os.environ['MY_STATE_MACHINE_ARN']
client = boto3.client('stepfunctions')


def handler(event, context):
    print(event)
    for record in event['Records']:
        trigger_workflow(record)


def trigger_workflow(event_record):
    response = client.start_execution(
        stateMachineArn=my_state_machine_arn,
        input=json.dumps(event_record['s3'])
    )