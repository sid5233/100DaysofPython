from http import client
from pydoc import cli
import boto3

client = boto3.client('ec2', region_name="eu-central-1")
resour = boto3.resource('ec2', region_name="eu-central-1")

newVPC = resour.create_vpc(
    CidrBlock="10.0.0.0/16"
)

newVPC.create_subnet(
    CidrBlock = "10.0.1.0/24"
)

newVPC.create_subnet(
    CidrBlock = "10.0.2.0/24"
)

newVPC.create_tags(
    Tags=[
        {   
        'Key': 'Name',
        'Value' : 'my-vpc'
        }
    ]
)

allVPC = client.describe_vpcs()
vpcs = allVPC["Vpcs"]
# print(vpcs)

for vpc in vpcs :
    print(vpc["VpcId"])