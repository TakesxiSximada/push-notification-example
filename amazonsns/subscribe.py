import enum
import argparse

import boto3


class SNSProtocol(enum.Enum):
    http = 'http'  # delivery of JSON-encoded message via HTTP POST
    https = 'https'  # delivery of JSON-encoded message via HTTPS POST
    email = 'email'  # delivery of message via SMTP
    email_json = 'email-json'  # delivery of JSON-encoded message via SMTP
    sms = 'sms'  # delivery of message via SMS
    sqs = 'sqs'  # delivery of JSON-encoded message to an Amazon SQS queue
    application = 'application'  # noqa : delivery of JSON-encoded message to an EndpointArn for a mobile app and device.


parser = argparse.ArgumentParser()
parser.add_argument('topic_arn')
parser.add_argument('endpoint_arns', nargs='+')
args = parser.parse_args()

topic_arn = args.topic_arn
endpoint_arns = args.endpoint_arns

client = boto3.client('sns')
for endpoint_arn in endpoint_arns:
    res = client.subscribe(
        TopicArn=topic_arn,
        Protocol=SNSProtocol.application.value,
        Endpoint=endpoint_arn,
    )
    print(res)
