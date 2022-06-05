import boto3
import string
import secrets
import json
from botocore.exceptions import ClientError

iam = boto3.client('iam')


def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def get_user_id():
    return boto3.client('sts').get_caller_identity().get('Account')


def create_login_profile(name):
    try:
        random_password = generate_random_password()
        iam.create_login_profile(
            UserName=name,
            Password=random_password,
            PasswordResetRequired=False
        )
        with open("cred.json", 'w') as file:
            file.write(json.dumps({
                'UserId': get_user_id(),
                'UserName': name,
                'Password': random_password
            }, indent=4))
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_login_profile("user_name")
