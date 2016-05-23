import argparse

import boto3
import botocore.exceptions


parser = argparse.ArgumentParser()
parser.add_argument('title')
parser.add_argument('message')
parser.add_argument('topic_arn')
args = parser.parse_args()

topic_arn = args.topic_arn
message = args.message
title = args.title

client = boto3.client('sns')
res = client.publish(
    TopicArn=topic_arn,
    Message=message,
    Subject=title,
    MessageStructure='raw',
)
print(res)
