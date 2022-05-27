import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')


def create_waiter(resource_type, resource_id):
    waiter = ec2.get_waiter(resource_type)
    waiter.wait(VpcIds=[resource_id])


def create_tags(resource_id, resource_name):
    ec2.create_tags(
        Resources=[resource_id],
        Tags=[{
            "Key": "Name",
            "Value": resource_name
        }]
    )


def create_vpc(cidr, vpc_name):
    try:
        response = ec2.create_vpc(CidrBlock=cidr)
        vpc_id = response.get("Vpc").get("VpcId")
        create_waiter("vpc_available", vpc_id)
        create_tags(vpc_id, vpc_name)
        print(f'vpc {vpc_name} with {cidr} has been created')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_vpc("cidr_block", "vpc_name")
