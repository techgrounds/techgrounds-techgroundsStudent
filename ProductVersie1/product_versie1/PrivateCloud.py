import aws_cdk as cdk 
from aws_cdk import aws_ec2 as ec2 


vpc = ec2.Vpc(self, "PriveWolk", max_azs=3)

