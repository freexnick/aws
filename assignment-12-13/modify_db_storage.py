import boto3
from botocore.exceptions import ClientError

rds = boto3.client('rds')


def modify_db_storage(db_name, size):
    try:
        rds.modify_db(
            DBInstanceIdentifier=db_name,
            StorageType='gp2',
            AllocatedStorage=size,
            ApplyImmediately=True,
        )
        print(f"{db_name} has been modified")
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    modify_db_storage("db_name", "storage_size")
