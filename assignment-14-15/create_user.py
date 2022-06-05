import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')


def create_user(name):
    try:
        response = iam.create_user(UserName=name)
        print(f"{name} user has been created")
        return response.get('User').get('UserName')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_user("user_name")
