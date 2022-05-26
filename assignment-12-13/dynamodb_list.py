import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def dynamodb_list():
    try:
        print(list(dynamodb.tables.all()))
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    dynamodb_list()
