import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_vpc_id(vpc_name):
    filter = [{'Name': 'tag:Name', 'Values': [vpc_name]}]
    return ec2.describe_vpcs(Filters=filter)['Vpcs'][0]["VpcId"]


def create_tags(group_id, sg_name):
    ec2.create_tags(
        Resources=[group_id],
        Tags=[{
            "Key": "Name",
            "Value": sg_name
        }]
    )


def create_security_group(vpc_name, sg_name, description):
    try:
        response = ec2.create_security_group(
            VpcId=get_vpc_id(vpc_name),
            GroupName=sg_name,
            Description=description,
        )
        group_id = response.get("GroupId")
        create_tags(group_id, sg_name)
        print(f' {sg_name} has been created')
        return group_id
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_security_group("vpc_name", "sg_name", "description")
