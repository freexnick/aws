import boto3
from botocore.exceptions import ClientError

rds = boto3.client('rds')


def create_db_snapshot(snapshot_name, db_name):
    try:
        rds.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_name,
            DBInstanceIdentifier=db_name,
            Tags=[{
                'Key': 'Name',
                'Value': snapshot_name}
            ]
        )
        print(f"{snapshot_name} snapshot has been created")
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_db_snapshot("snapshot_name", "db_name")
