import boto3
from botocore.exceptions import ClientError

rds = boto3.client('rds')


def determine_port(db_engine):
    match db_engine.lower():
        case "aurora" | "mysql" | "mariadb":
            return 3306
        case "postgre" | "postgresql":
            return 5432
        case "oracle":
            return 1521
        case "sql" | "sql server":
            return 1433
        case default:
            return


def create_db_instance(name, engine, storage='60', username='admin', password='admin'):
    try:
        rds.create_db_instance(
            DBName=name,
            DBInstanceIdentifier=name,
            AllocatedStorage=storage,
            DBInstanceClass='db.t2.micro',
            Engine=engine,
            MasterUsername=username,
            MasterUserPassword=password,
            BackupRetentionPeriod=7,
            Port=determine_port(engine),
            MultiAZ=False,
            AutoMinorVersionUpgrade=True,
            PubliclyAccessible=True,
            Tags=[
                {
                    'Key': 'Name',
                    'Value': name
                },
            ],
            StorageType='gp2',
            DeletionProtection=False,
        )
        print(f"{name} has been created")
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    create_db_instance("db_name", 'db_engine', 'storage_size',
                       'db_username', 'db_password')
