import boto3

# User input for bucket name and file path
bucket = input("Enter Bucket Name : ")
file = input("Enter Object Name (Along with path if it is in subdirectory) : ")

# Connecting s3 as resource 
s3 = boto3.resource('s3')

# Retriving all versions of that object
versions = s3.Bucket(bucket).object_versions.filter(Prefix=file)

# Temporary List to get all versions
temp = []

# Appending all versions 
for version in versions:
	temp.append(version.get().get('VersionId'))

# Download the required file by providing the required version id (here second latest)
try:
    s3.Bucket(bucket).download_file(file, 'downloaded', ExtraArgs={'VersionId': temp[1]})

# If error occurs due to any reason
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
