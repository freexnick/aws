import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_vpc_id(vpc_name):
    filter = [{'Name': 'tag:Name', 'Values': [vpc_name]}]
    return ec2.describe_vpcs(Filters=filter)['Vpcs'][0]["VpcId"]


def create_tags(vpc_id, vpc_name):
    ec2.create_tags(
        Resources=[vpc_id],
        Tags=[{
            "Key": "Name",
            "Value": vpc_name
        }]
    )


def create_route_table(vpc_name, table_name):
    try:
        vpc_id = get_vpc_id(vpc_name)
        response = ec2.create_route_table(VpcId=vpc_id)
        route_id = response.get("RouteTable").get("RouteTableId")
        create_tags(route_id, table_name)
        print(f'{table_name} has been created')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_route_table("vpc_name",  "table_name")
