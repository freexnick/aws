import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')


def get_vpc_id(vpc_name):
    filter = [{'Name': 'tag:Name', 'Values': [vpc_name]}]
    return ec2.describe_vpcs(Filters=filter)['Vpcs'][0]["VpcId"]


def get_igw_id(igw_name):
    filter = [{'Name': 'tag:Name', 'Values': [igw_name]}]
    return ec2.describe_internet_gateways(
        Filters=filter)["InternetGateways"][0]["InternetGatewayId"]


def attach_vpc_to_igw(vpc_name, igw_name):
    try:
        vpc_id = get_vpc_id(vpc_name)
        igw_id = get_igw_id(igw_name)
        ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
        print(f'{vpc_name} has been attached to {igw_name}')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    attach_vpc_to_igw("vpc_name", "igw_name")
