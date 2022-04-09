import boto3

s3 = boto3.client('s3')


def get_buckets(bucket_name=""):
    response = s3.list_buckets()['Buckets']
    if bucket_name:
        match = [s for s in response if s['Name'].__contains__(
            bucket_name.lower())]
        if match:
            print("found matching buckets:")
            for bucket in match:
                print(f'{bucket["Name"]}')
        else:
            print("no bucket with such a name!")
    else:
        for bucket in response:
            print(f'{bucket["Name"]}')


if __name__ == '__main__':
    get_buckets("prod")
