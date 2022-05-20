import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_sg_id(sg_name):
    filter = [{'Name': 'tag:Name', 'Values': [sg_name]}]
    return ec2.describe_security_groups(Filters=filter)['SecurityGroups'][0]["GroupId"]


def get_subnet_id(subnet_name):
    filter = [{'Name': 'tag:Name', 'Values': [subnet_name]}]
    return ec2.describe_subnets(
        Filters=filter)["Subnets"][0]["SubnetId"]


def create_ec2_ft(sg_name, sub_name, key, ec2_name):
    try:
        ec2.run_instances(
            BlockDeviceMappings=[
                {
                    "DeviceName": "/dev/sdh",
                    "Ebs": {"DeleteOnTermination": True,
                            "VolumeSize": 10,
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
                        get_sg_id(sg_name),
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


if __name__ == '__main__':
    create_ec2_ft("sg_name", "sub_name", "key_name", "ec2_name")
