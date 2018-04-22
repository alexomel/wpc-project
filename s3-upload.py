import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('alexo-test-wpc')
my_file=open('to_be_uploaded.txt', 'w+')
my_file.write('test content')
my_file.close()

bucket.put_object(
        Key='test.txt',
        Body=open('./to_be_uploaded.txt', 'rb')
)
