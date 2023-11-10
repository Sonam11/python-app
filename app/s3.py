import os
import boto3

def s3_read():
	ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
	full_path_to_file = os.path.join(ROOT_DIR, "ping.txt")
	s3_read_service = boto3.client('s3')
	result = s3.get_buck_acl(Bucket='ujha-dev-us2')
	return result
