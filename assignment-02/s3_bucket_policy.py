import json
import boto3
from pprint import pprint
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def check_policy(bucket_name):
    try:
        response = s3.get_bucket_policy(Bucket=bucket_name)
        pprint(response.get('Policy'))
    except ClientError as e:
        return apply_policy(bucket_name)


def generate_public_read_policy(bucket_name):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                'Resource': [
                    f'arn:aws:s3:::{bucket_name}/dev/*',
                    f'arn:aws:s3:::{bucket_name}/test/*',
                ],
            }
        ]
    })


def apply_policy(bucket_name):
    if s3.put_bucket_policy(Bucket=bucket_name,
                            Policy=generate_public_read_policy(bucket_name)):
        print(f'policy has been applied to {bucket_name}')


if __name__ == '__main__':
    check_policy('btu-devops-nk-2022222')
