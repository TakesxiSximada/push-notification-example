import argparse

import boto3
import botocore.exceptions


parser = argparse.ArgumentParser()
parser.add_argument('user_name')
parser.add_argument('application_arn')
parser.add_argument('device_token')
args = parser.parse_args()

user_name = args.user_name
application_arn = args.application_arn
device_token = args.device_token

client = boto3.client('sns')
res = client.create_platform_endpoint(
    PlatformApplicationArn=application_arn,
    Token=device_token,
    CustomUserData=user_name,
    )
print(res)
