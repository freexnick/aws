from multiprocessing.connection import Client
import boto3

from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def get_webendpoint(bucket_name):
    try:
        zone = s3.head_bucket(Bucket=bucket_name)['ResponseMetadata']['HTTPHeaders'][
            'x-amz-bucket-region']
        print(f'http://{bucket_name}.s3-website-{zone}.amazonaws.com')
    except ClientError as e:
        print(e)


if __name__ == '__main__':
    get_webendpoint('demo.btu-nk-2022.com',)
