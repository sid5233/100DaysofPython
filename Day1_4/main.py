from http import client
from pydoc import cli
import boto3

client = boto3.client('ec2', region_name="eu-central-1")

allVPC = client.describe_vpcs()
vpcs = allVPC["Vpcs"]
# print(vpcs)

for vpc in vpcs :
    print(vpc["VpcId"])