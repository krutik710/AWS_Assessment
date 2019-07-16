# Step 1 :

# Create a lambda function 'assessment-name'
# Attach following code in it :


import json


def lambda_handler(event, context):

    # Just returning the name from event

    return {

        'statusCode': 200,

        'body': event['name']

    }




# Step 2:

# Create API gateway.
# Give name to the API and create a new API
# Create a resourse name name
# Create a GET method in the name resource
# Add a URL query string in method request
# Add 'name' in URL query string and check the required box
# Make a content-type named ‘application/json’
# Create an empty template for application/json and add following code in it:
# #set($inputRoot = $input.path('$'))
# { 
# "name" : "$input.params('name')"
# }

# Deploy the API and name the stage test
# Copy paste the URL in the web browser.


