import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def create_key_pair(name):
    try:
        response = ec2.create_key_pair(
            KeyName=name,
            KeyType="rsa",
        )
        with open(f"{name}.pem", "w") as file:
            file.write(response.get("KeyMaterial"))
        print(f"{name} Key has been crated")
        return response.get("KeyPairId")
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_key_pair("key_name")
