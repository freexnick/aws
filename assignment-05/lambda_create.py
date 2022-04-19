import boto3
from pathlib import Path
from botocore.exceptions import ClientError

client = boto3.client('lambda')
iam = boto3.client('iam')


def convert_to_bytes(zip_file):
    with open(zip_file, 'rb') as file_data:
        bytes_content = file_data.read()
    return bytes_content


def create_function(function_name, iam_role, function_handler, zip_file):
    try:
        client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role=iam.get_role(RoleName=iam_role)['Role']['Arn'],
            Handler=f'{Path(zip_file).stem}.{function_handler}',
            Code={
                'ZipFile': convert_to_bytes(zip_file)
            },
        )
        print(f'function {function_name} has been created')
    except ClientError as e:
        print(e)


if __name__ == '__main__':
    create_function('lambda-image-processor', 'LabRole',
                    'lambda_handler', './lambda_image_processor.zip')
