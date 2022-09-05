import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')


def create_tags(resource_id, tags):
    ec2.create_tags(
        Resources=[resource_id],
        Tags=tags
    )


def create_vpc(cidr, vpc_name):
    try:
        response = ec2.create_vpc(CidrBlock=cidr)
        vpc_id = response.get("Vpc").get("VpcId")
        create_tags(vpc_id, [{
            "Key": "Name",
            "Value": vpc_name,
        }, {"Key": "Creator",
            "Value": "Nika"}])
        print(f'vpc {vpc_name} with {cidr} has been created')
        return vpc_id
    except ClientError as e:
        print(e)
        return


def create_subnet(vpc_id, cidr, subnet_name):
    try:
        response = ec2.create_subnet(CidrBlock=cidr, VpcId=vpc_id)
        subnet_id = response.get("Subnet").get("SubnetId")
        create_tags(subnet_id, [{
            "Key": "Name",
            "Value": subnet_name
        }])
        print(f'{subnet_name} with {cidr} has been created')
        return subnet_id
    except ClientError as e:
        print(e)
        return


def create_route_table(vpc_id, table_name):
    try:
        response = ec2.create_route_table(VpcId=vpc_id)
        route_id = response.get("RouteTable").get("RouteTableId")
        create_tags(route_id, [{
            "Key": "Name",
            "Value": table_name
        }])
        print(f'{table_name} has been created')
        return route_id
    except ClientError as e:
        print(e)
        return


def associate_sub_with_rt(subnet_id, table_id):
    try:
        ec2.associate_route_table(RouteTableId=table_id, SubnetId=subnet_id)
        print(f'{subnet_id} has been associated with {table_id}')
    except ClientError as e:
        print(e)
        return


def main():
    vpc_id = create_vpc("10.10.0.0/16", "vpc_name")
    pub_sub_id = create_subnet(vpc_id, "10.10.1.0/24", "public-subnet")
    pri_sub_id = create_subnet(vpc_id, "10.10.2.0/24", "private-subnet")
    pub_rt_id = create_route_table(vpc_id, "public")
    pri_rt_id = create_route_table(vpc_id, "private")
    associate_sub_with_rt(pub_sub_id, pub_rt_id)
    associate_sub_with_rt(pri_sub_id, pri_rt_id)


if __name__ == '__main__':
    main()
