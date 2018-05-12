import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('alexo-test-wpc')
my_file=open('file.txt', 'w+')
my_file.write('test content')
my_file.close()

bucket.put_object(
        Key='file.txt',
        Body=open('./file.txt', 'rb')
)
