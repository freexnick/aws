import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def create_igw(igw_name):
    try:
        ec2.create_internet_gateway(TagSpecifications=[{
            "ResourceType": "internet-gateway",
            "Tags": [
                {"Key": "Name",
                 "Value": igw_name}
            ]
        }])
        print(f'{igw_name} has been created')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_igw("igw_name")
