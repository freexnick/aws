import boto3
import argparse
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--vpc')
    parser.add_argument('-s', '--subnet')
    return parser.parse_args()


def get_vpc_id(vpc_name):
    filter = [{'Name': 'tag:Name', 'Values': [vpc_name]}]
    return ec2.describe_vpcs(Filters=filter)['Vpcs'][0]["VpcId"]


def get_subnet_id(subnet_name):
    filter = [{'Name': 'tag:Name', 'Values': [subnet_name]}]
    return ec2.describe_subnets(
        Filters=filter)["Subnets"][0]["SubnetId"]


def create_security_group(vpc_name, sg_name):
    try:
        response = ec2.create_security_group(
            VpcId=get_vpc_id(vpc_name),
            GroupName=sg_name,
            Description=sg_name,
        )
        group_id = response.get("GroupId")
        print(f'{sg_name} has been created')
        return group_id
    except ClientError as e:
        print(e)
        return


def add_rule_to_sg(sg_id, ip_address, port):
    try:
        ec2.authorize_security_group_ingress(
            CidrIp=ip_address,
            FromPort=port,
            GroupId=sg_id,
            IpProtocol='tcp',
            ToPort=port,
        )
        print("rule has been added")
    except ClientError as e:
        print(e)
        return


def create_key_pair(name):
    try:
        response = ec2.create_key_pair(
            KeyName=name,
            KeyType="rsa",
        )
        with open(f"{name}.pem", "w") as file:
            file.write(response.get("KeyMaterial"))
        print(f"{name} Key has been crated")
        return name
    except ClientError as e:
        print(e)
        return


def create_ec2_ft(sg_id, sub_name, key, ec2_name, vol_size):
    try:
        ec2.run_instances(
            BlockDeviceMappings=[
                {
                    "DeviceName": "/dev/sdh",
                    "Ebs": {"DeleteOnTermination": True,
                            "VolumeSize": vol_size,
                            "VolumeType": "gp2",
                            "Encrypted": False},
                },
            ],
            ImageId="ami-0022f774911c1d690",
            InstanceType="t2.micro",
            KeyName=key,
            MaxCount=1,
            MinCount=1,
            Monitoring={"Enabled": True},
            InstanceInitiatedShutdownBehavior="stop",
            NetworkInterfaces=[
                {
                    "AssociatePublicIpAddress": True,
                    "DeleteOnTermination": True,
                    "Groups": [
                        (sg_id),
                    ],
                    "DeviceIndex": 0,
                    "SubnetId": get_subnet_id(sub_name),
                },
            ],
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': ec2_name,
                        },
                    ]
                },
            ],
        )
        print("ec2 has been launched")
    except ClientError as e:
        print(e)
        return


def main():
    parser = init_argparse()
    sg_id = create_security_group(parser.vpc, parser.subnet)
    add_rule_to_sg(sg_id, "0.0.0.0/0", 22)
    add_rule_to_sg(sg_id, "0.0.0.0/0", 80)
    key_name = create_key_pair("final-exam-ec2s-private")
    create_ec2_ft(sg_id, parser.subnet,
                  key_name, "exam-test", 10)
    create_ec2_ft(sg_id, parser.subnet,
                  key_name, "exam-test", 40)


if __name__ == '__main__':
    main()
