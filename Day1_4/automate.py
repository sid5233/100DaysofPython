from operator import truediv
import boto3
import schedule
    
    
ec2Client = boto3.client('ec2')
ec2Resource = boto3.resource('ec2')


def checkStatus():
    res = ec2Client.describe_instances()
    for reservation in res["Reservations"]:
        instances = reservation["Instances"]
        for inst in instances:
            print(f"Instance {inst['InstanceId']} is {inst['State']['Name']}") 
            
schedule.every(10).seconds.do(checkStatus)

while True:
    schedule.run_pending()