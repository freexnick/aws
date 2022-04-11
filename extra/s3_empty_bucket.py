import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')


def empty_bucket(bucket_name):
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        print(f'bucket {bucket_name} has been cleaned up')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    empty_bucket('btu-devops-nk-2022')
