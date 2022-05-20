import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_sg_id(sg_name):
    filter = [{'Name': 'tag:Name', 'Values': [sg_name]}]
    return ec2.describe_security_groups(Filters=filter)['SecurityGroups'][0]["GroupId"]


def add_rule_to_sg(sg_name, ip_address, port):
    try:
        ec2.authorize_security_group_ingress(
            CidrIp=ip_address,
            FromPort=port,
            GroupId=get_sg_id(sg_name),
            IpProtocol='tcp',
            ToPort=port,
        )
        print("rule has been added")
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    add_rule_to_sg("sg_name", "ip", "port")
