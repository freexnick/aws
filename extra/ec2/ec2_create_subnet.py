import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_vpc_id(vpc_name):
    filter = [{'Name': 'tag:Name', 'Values': [vpc_name]}]
    return ec2.describe_vpcs(Filters=filter)['Vpcs'][0]["VpcId"]


def create_waiter(resource_type, resource_id):
    waiter = ec2.get_waiter(resource_type)
    waiter.wait(SubnetIds=[resource_id])


def create_tags(vpc_id, vpc_name):
    ec2.create_tags(
        Resources=[vpc_id],
        Tags=[{
            "Key": "Name",
            "Value": vpc_name
        }]
    )


def create_subnet(vpc_name, cidr, subnet_name):
    try:
        vpc_id = get_vpc_id(vpc_name)
        response = ec2.create_subnet(CidrBlock=cidr, VpcId=vpc_id)
        subnet_id = response.get("Subnet").get("SubnetId")
        create_waiter("subnet_available", subnet_id)
        create_tags(subnet_id, subnet_name)
        print(f'{subnet_name} with {cidr} has been created')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_subnet("vpc_name", "cidr_block", "subnet_name")
