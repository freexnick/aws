import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def delete_file(bucket_name, file_name):
    try:
        s3.delete_object(Bucket=bucket_name, Key=file_name)
    except ClientError as e:
        print(e)
        return
    print('file has been deleted')


if __name__ == '__main__':
    delete_file('btu-devops-nk-2023', 'IMG_1002.JPG')
