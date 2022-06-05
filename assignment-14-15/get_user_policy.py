from pprint import pprint
from botocore.exceptions import ClientError
import boto3

iam = boto3.client('iam')


def get_user_policy(user_name):
    try:
        pprint(iam.get_user(
            UserName=user_name,
        ))
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    get_user_policy('user1654088=nikolozi.kapanadze.1@btu.edu.ge')
