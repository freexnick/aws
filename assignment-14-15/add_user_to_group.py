import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')


def add_user_to_group(username, group):
    try:
        iam.add_user_to_group(UserName=username, GroupName=group)
        print(f"{username} has been added to {group}")
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    add_user_to_group("user_name", "group_name")
