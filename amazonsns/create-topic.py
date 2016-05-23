import argparse

import boto3
import botocore.exceptions


parser = argparse.ArgumentParser()
parser.add_argument('topic_name')
args = parser.parse_args()

topic_name = args.topic_name

client = boto3.client('sns')
res = client.create_topic(Name=topic_name)
print(res)
