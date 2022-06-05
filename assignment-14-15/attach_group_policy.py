import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')


def attach_group_policy(group, policy):
    try:
        iam.attach_group_policy(GroupName=group, PolicyArn=policy)
        print(f"{policy} has been added to {group}")
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    attach_group_policy("group_name", "policy_arn")
