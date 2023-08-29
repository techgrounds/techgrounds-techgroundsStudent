import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class deCloud(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creëer een VPC voor de webserver
        vpc_app = ec2.Vpc(self, "app-prd-vpc", 
                      nat_gateways=0,
                      max_azs=2,
                      ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/24"),
                      subnet_configuration=[ec2.SubnetConfiguration(name="Publiek",subnet_type=ec2.SubnetType.PUBLIC)], 
                     
            )
        
        # Creëer een VPC voor de Management server
       
       
        # Creëer een webserver binnen "app-prd-vpc"
        
        # app_server = ec2.Instance(self, "app_server")
        
                      





