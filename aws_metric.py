import hug
from boto.ec2 import autoscale
from boto import ec2
from boto import rds

# @hug.local()
@hug.post('/autoscale/running/count')
def get_running_instance_count(body):
	"""Function to get running rds instance count
	
	Args:
	    body (json string): post body in json string

	Returns:
	    TYPE: Description
	"""
	body = dict(body)
	conn = autoscale.connect_to_region(region_name='us-west-2',
								aws_access_key_id=body["aws_access_key_id"],
								aws_secret_access_key=body["aws_secret_access_key"])
	instance_status = conn.get_all_autoscaling_instances()
	running_instances = 0
	for item in instance_status:
		if (item.health_status == 'HEALTHY'):
			running_instances += 1
	return {"data":running_instances}

# @hug.local()
@hug.post('/ec2/running/count')
def get_running_instance_count(body):
	"""Function to get running ec2 instance count
	
	Args:
	    body (json string): post body in json string

	Returns:
	    TYPE: Description
	"""
	body = dict(body)
	conn = ec2.connect_to_region(region_name='us-west-2',
								aws_access_key_id=body["aws_access_key_id"],
								aws_secret_access_key=body["aws_secret_access_key"])
	instance_status = conn.get_all_instance_status()
	running_instances = 0
	for item in instance_status:
		if (item.state_name == 'running'):
			running_instances += 1
	return {"data":running_instances}

# @hug.local()
@hug.post('/rds/running/count')
def get_running_instance_count(body):
	"""Function to get running rds instance count
	
	Args:
	    body (json string): post body in json string

	Returns:
	    TYPE: Description
	"""
	body = dict(body)
	conn = rds.connect_to_region(region_name='us-west-2',
								aws_access_key_id=body["aws_access_key_id"],
								aws_secret_access_key=body["aws_secret_access_key"])
	instance_status = conn.get_all_dbinstances()
	running_instances = 0
	for item in instance_status:
		if (item.state_name == 'available'):
			running_instances += 1
	return {"data":running_instances}