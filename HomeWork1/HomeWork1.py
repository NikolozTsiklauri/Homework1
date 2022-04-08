import boto3

s3 = boto3.client('s3')

def main():
    response = s3.list_buckets()

    print('List of buckets:')
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')

def List_Bucket_Start_with_Prod():
    response = s3.list_buckets()
    print("Bucket list with 'prod':")
    for bucketwithprod in response['Buckets']:
        if bucketwithprod["Name"].startswith('prod'):
            print(f'{bucketwithprod["Name"]}')



if __name__=='__main__':
    main()
    List_Bucket_Start_with_Prod()
