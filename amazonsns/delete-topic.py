import argparse

import boto3
import botocore.exceptions


parser = argparse.ArgumentParser()
parser.add_argument('topic_arn')
args = parser.parse_args()

topic_arn = args.topic_arn

client = boto3.client('sns')
res = client.delete_topic(TopicArn=topic_arn)
print(err)
