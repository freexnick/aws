import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def upload_file(input_name, bucket_name, output_name):
    with open(input_name, 'rb') as file:
        try:
            s3.upload_fileobj(file, bucket_name, output_name)
        except ClientError as e:
            print(e)
            return
        print('file has been uploaded')


if __name__ == '__main__':
    upload_file("./src/IMG_1002.JPG", 'btu-devops-nk-2023', 'IMG_1003.JPG')
