from fileinput import filename
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def download_file(bucket_name, file_name, path=""):
    try:
        s3.download_file(Bucket=bucket_name, Key=file_name,
                         Filename=path + '/' + file_name if path else file_name)
    except ClientError as e:
        print(e)
        return
    print(f'file {file_name} has been downloaded')


if __name__ == '__main__':
    download_file('btu-devops-nk-2023', 'IMG_1002.JPG', '../src/')
