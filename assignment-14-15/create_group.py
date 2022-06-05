import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')


def create_group(name):
    try:
        response = iam.create_group(GroupName=name)
        print(f"{name} group has been created")
        return response.get('Group').get('Name')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_group("group_name")
