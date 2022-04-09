import boto3
import os
import mimetypes
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def guess_file_type(file):
    file_type, _,  = mimetypes.guess_type(file)
    return "binary/octet-stream" if file_type is None else file_type


def upload_directory(bucket_name, path):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file).split(
                './')[-1].replace('\\', '/')
            try:
                s3.upload_file(file_path,
                               bucket_name, file_path, ExtraArgs={
                                   "ContentType": guess_file_type(file_path)
                               }),
            except ClientError as e:
                print(e)
                return
    print('files have been uploaded')


if __name__ == '__main__':
    upload_directory('demo.btu-nk-2022.com', './website/')
