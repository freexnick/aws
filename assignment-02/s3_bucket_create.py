import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def check_bucket(bucket_name):
    try:
        response = s3.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        print(e)
        return False
    return response['ResponseMetadata']['HTTPStatusCode'] == 200


def create_bucket(bucket_name):
    if not check_bucket(bucket_name):
        try:
            s3.create_bucket(Bucket=bucket_name)
            print(f'Bucket named {bucket_name} has been created successfully')
        except ClientError as e:
            print(f'failed to create bucket,reason: {e}')
    else:
        print(f'{bucket_name} already exists')


if __name__ == '__main__':
    create_bucket('btu-devops-nk-2023')
