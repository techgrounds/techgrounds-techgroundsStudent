import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class deCloud(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

       
    #    Maak een s3-bucket die encrypted is 
       
       
       # Creëer een VPC voor de webserver
        vpc_app = ec2.Vpc(self, id = "app-prd-vpc", 
                      nat_gateways=0,
                      max_azs=2,
                      ip_addresses = ec2.IpAddresses.cidr("10.10.0.0/24"),
                      subnet_configuration=[ec2.SubnetConfiguration(name="Publiek",subnet_type=ec2.SubnetType.PUBLIC)], 
                     
            )
     
       # Creëer een SG voor de webserver
        sg_webserver = ec2.SecurityGroup(self,"sgWebServer", 
                                         vpc = vpc_app,
                                         description = "sg_webserver vanuit CDK"
                                         allow_all_outbound=True,
                                                                                 
                                         )
        sg_webserver.add_ingress_rule()
        
     
        # Creëer een webserver binnen "app-prd-vpc" die draait op Windows 
        
        app_server = ec2.Instance(self, name = "app_server", 
                                  vpc = vpc_app, 
                                  instance_type = ec2.InstanceType('t3a.micro'),
                                  machine_image = ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE)
                                  security_group = sg_webserver
                                  
        )
        # webserver moet via http en https toegankelijk zijn 
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Wereldwijd toegankelijk")
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Wereldwijd toegankelijk")
        
        
        
        
        # Creëer een VPC voor de Management server
        
        vpc_admin_server = ec2.Vpc(self, "management-prd-vpc", 
                                     ec2.IIp_addresses.cidr("10.20.20.0/24"), 
                                     
                                                          )
        
        # Creëer een SG voor de admin-server
        
        # Creëer een management-server binnen de VPC management-prd-vpc, deze zal werken op Linux
        
        #    Creëer een ACL voor de admin-server
          #    Creëer een ACL voor de app-server
                                  
                                  
        
                      





