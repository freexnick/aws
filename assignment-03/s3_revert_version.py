import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def revert_version(bucket_name, file_name):
    try:
        response = s3.list_object_versions(
            Bucket=bucket_name, Prefix=file_name)['Versions']
        copy_source = {
            'Bucket': bucket_name,
            'Key': response[1]['Key'],
            'VersionId': response[1]['VersionId']
        }
        s3.copy_object(CopySource=copy_source, Bucket=bucket_name,
                       Key=copy_source['Key'], )
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    revert_version('btu-devops-nk-2022', 'v1')
