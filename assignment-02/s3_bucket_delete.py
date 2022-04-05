import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def check_bucket(bucket_name):
    try:
        response = s3.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        print(e)
        print(f"Bucket {bucket_name} doesn't exist")
        return False
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return delete_bucket(bucket_name)


def delete_bucket(bucket_name):
    s3.delete_bucket(Bucket=bucket_name)
    print(f'Bucket named {bucket_name} has been successfully deleted')


if __name__ == '__main__':
    check_bucket('btu-devops-nk-2022222')
