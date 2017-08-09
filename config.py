import os
try:
	aws_access_key_id = os.environ['aws_key']
	aws_secret_access_key = os.environ['aws_secret']
except KeyError:
	print("environment variables missing for aws_key and aws_secret")


