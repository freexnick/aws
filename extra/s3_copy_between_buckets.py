import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def copy_to_bucket(source_bucket, file, destination_bucket):
    copy_source = {
        'Bucket': source_bucket,
        'Key': file
    }
    try:
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket,
                       Key=file, )
    except ClientError as e:
        print(e)


if __name__ == '__main__':
    copy_to_bucket('btu-devops-nk-2022', 'my_file.txt', 'btu-devops-nk-2023')
