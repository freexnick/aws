import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def get_instance_id(instance_name):
    filter = [{'Name': 'tag:Name', 'Values': [instance_name]}]
    return ec2.describe_instances(Filters=filter)['Reservations'][0]['Instances'][0]['InstanceId']


def ec2_instance_terminate(instance_name):
    try:
        ec2.terminate_instances(
            InstanceIds=[
                get_instance_id(instance_name),
            ],
        )
        print(f'{instance_name} has been terminated')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    ec2_instance_terminate("ec2_name")
