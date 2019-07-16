import boto3

from boto3.dynamodb.conditions import Key, Attr

# Get the service resource
dynamodb = boto3.setup_default_session(region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')


try:
	table = dynamodb.Table('Krutik_Games')

	response = table.query(
	    KeyConditionExpression=Key('gid').eq(2)
	)

	items = response['Items']

	print("GNAME")
	print("RATING")


	for item in items:
		name = item[u'gname']
	        rat = item[u'rating']
	        print(name,end="  ")
	        print(rat)

except Exception as e:
    print('Table Not Found')
