import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb')


def dynamodb_get_table(table_name, file_name):
    try:
        response = dynamodb.scan(TableName=table_name)
        with open(f"{file_name}.txt", "w") as file:
            for item in response['Items']:
                file.write("{}\n".format(item))
        print(f'{table_name} items have been saved to {file_name}')
    except ClientError as e:
        print(e)
        return


if __name__ == '__main__':
    dynamodb_get_table("test", "file_name")
