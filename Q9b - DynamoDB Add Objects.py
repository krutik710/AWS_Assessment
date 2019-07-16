import boto3

dynamodb = boto3.setup_default_session(region_name='us-east-1')

dynamodb = boto3.resource('dynamodb')


try:
	table = dynamodb.Table('Krutik_Games')
	# Insert Items into table
	table.put_item(
	   Item={
	        'gid': 2,
	        'gname': 'DKAM',
	        'publisher': 'All Star Heaven',
	        'rating':9,
	        'release_date': '2019-07-15',
	        'genres':{'drama','thriller'}
	        }
	)
	# Completion Message
	print('Data Inserted Successfully')
	
except Exception as e:
    print('Table Not Found')
