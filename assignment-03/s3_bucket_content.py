import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def get_bucket_content(bucket_name):
    files = {}
    try:
        result = s3.list_objects(Bucket=bucket_name)
        for result in result.get("Contents", []):
            extension = (result.get("Key").split(".")[-1])
            if extension in files.keys():
                files[extension] = files.get(extension) + 1
            else:
                files[extension] = 1
        print(files)
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    get_bucket_content('btu-devops-nk-2022')
