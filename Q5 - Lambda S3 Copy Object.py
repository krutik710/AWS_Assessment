import json
import boto3



def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client('s3')

    # Specify the source destination bucket
    dest_bucket = "krutik-destination"

    # Get the object name and bucket name
    key = event["Records"][0]["s3"]["object"]["key"]
    bucket=event["Records"][0]["s3"]["bucket"]["name"]

    # Copy Object 
    s3.copy_object(Bucket=dest_bucket,Key=key,CopySource={'Bucket':bucket,'Key':key})

    # Return response
    return {
        'statusCode': 200,
        'body': event["Records"][0]["s3"]["object"]["key"]
    }