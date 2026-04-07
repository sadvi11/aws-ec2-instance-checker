import boto3
import json
from datetime import datetime

def check_ec2_instances():
    ec2 = boto3.client('ec2', region_name='ca-central-1')
    
    print("Connecting to AWS EC2...")
    response = ec2.describe_instances()
    
    instances = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            data = {
                'instance_id': instance['InstanceId'],
                'instance_type': instance['InstanceType'],
                'state': instance['State']['Name'],
                'region': 'ca-central-1',
                'launch_time': str(instance['LaunchTime'])
            }
            instances.append(data)
            print(f"Found: {data['instance_id']} | {data['instance_type']} | {data['state']}")
    
    if not instances:
        print("No EC2 instances found in this region.")
    
    report = {
        'generated_at': str(datetime.now()),
        'total_instances': len(instances),
        'instances': instances
    }
    
    with open('ec2_report.json', 'w') as f:
        json.dump(report, f, indent=4)
    
    print(f"\nReport saved to ec2_report.json")
    print(f"Total instances found: {len(instances)}")

check_ec2_instances()
