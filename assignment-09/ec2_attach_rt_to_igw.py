import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_table_id(table_name):
    filter = [{'Name': 'tag:Name', 'Values': [table_name]}]
    return ec2.describe_route_tables(
        Filters=filter)["RouteTables"][0]["RouteTableId"]


def get_igw_id(igw_name):
    filter = [{'Name': 'tag:Name', 'Values': [igw_name]}]
    return ec2.describe_internet_gateways(
        Filters=filter)["InternetGateways"][0]["InternetGatewayId"]


def attach_rt_to_igw(table_name, igw_name):
    try:
        route_id = get_table_id(table_name)
        igw_id = get_igw_id(igw_name)
        ec2.create_route(
            DestinationCidrBlock="0.0.0.0/0",
            RouteTableId=route_id,
            GatewayId=igw_id
        )
        print(f'route to {igw_name} has been added to {table_name}')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    attach_rt_to_igw("table_name",  "igw_name")
