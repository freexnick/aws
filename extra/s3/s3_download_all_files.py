import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


def download_file(bucket_name, file_name, path="./"):
    file_path = path + "/" + file_name if path else file_name
    try:
        if not os.path.exists(path) and path:
            os.makedirs(path)
        if file_name:
            s3_client.download_file(Bucket=bucket_name, Key=file_path,
                                    Filename=file_path)
    except ClientError as e:
        print(e)
        return
    print(f'file {file_name} has been downloaded')


def download_all_files(bucket_name):
    try:
        bucket = s3.Bucket(bucket_name)
        for item in bucket.objects.all():
            path, file = os.path.split(item.key)
            download_file(bucket_name, file, path)
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    download_all_files('btu-devops-nk-2022')
