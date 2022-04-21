import boto3

from botocore.exceptions import ClientError

s3 = boto3.client('s3')
client = boto3.client('lambda')

file_extensions = ['.jpg', '.jpeg', '.png']


def add_permision(function_name, bucket_name):
    client.add_permission(
        FunctionName=function_name,
        StatementId='1',
        Action='lambda:InvokeFunction',
        Principal='s3.amazonaws.com',
        SourceArn=f'arn:aws:s3:::{bucket_name}',
    )


def s3_trigger(bucket_name, function_name):
    lambda_foreach = []
    for extension in file_extensions:
        lambda_foreach.append({
            'LambdaFunctionArn': client.get_function(
                FunctionName=function_name)['Configuration']['FunctionArn'],
            'Events': [
                's3:ObjectCreated:*'
            ],
            'Filter': {
                'Key': {
                    'FilterRules': [
                        {
                            'Name': 'suffix',
                            'Value': extension
                        },
                    ]
                }
            }
        },)
    try:
        add_permision(function_name, bucket_name)
        s3.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration={
                'LambdaFunctionConfigurations': lambda_foreach,
            }
        )
        print(f'{function_name} has been added to {bucket_name}')
    except ClientError as e:
        print(e)


if __name__ == '__main__':
    s3_trigger('btu-devops-nk-2023',
               'lambda-image-processor',
               )
