import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_table_id(table_name):
    filter = [{'Name': 'tag:Name', 'Values': [table_name]}]
    return ec2.describe_route_tables(
        Filters=filter)["RouteTables"][0]["RouteTableId"]


def get_subnet_id(subnet_name):
    filter = [{'Name': 'tag:Name', 'Values': [subnet_name]}]
    return ec2.describe_subnets(
        Filters=filter)["Subnets"][0]["SubnetId"]


def associate_sub_with_rt(subnet_name, table_name):
    try:
        table_id = get_table_id(table_name)
        subnet_id = get_subnet_id(subnet_name)
        ec2.associate_route_table(RouteTableId=table_id, SubnetId=subnet_id)
        print(f'{subnet_name} has been associated with {table_name}')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    associate_sub_with_rt("subnet_name", "table_name")
