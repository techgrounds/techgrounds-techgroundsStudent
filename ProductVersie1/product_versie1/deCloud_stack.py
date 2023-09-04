import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3, 
    aws_kms as kms,
    aws_backup as backup,
    aws_iam as iam
)
from constructs import Construct

class deCloud(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

       
    #   Maak een s3-bucket die encrypted is 
        deEmmer = s3.Bucket(self, "VersleuteldeEmmer",
        bucket_name = "s3-bucket4scripts",
        access_control = s3.BucketAccessControl.PRIVATE,
        encryption = s3.BucketEncryption.KMS,
        versioned = True,
        block_public_access = s3.BlockPublicAccess.BLOCK_ALL
    )
        assert isinstance(deEmmer.encryption_key, kms.Key)

       
       # Creëer een VPC voor de webserver
        vpc_app = ec2.Vpc(self, id = "app-prd-vpc", 
                      nat_gateways=0,
                      max_azs=2,
                      ip_addresses = ec2.IpAddresses.cidr("10.10.0.0/24"),
                      subnet_configuration=[ec2.SubnetConfiguration(name="Publiek",subnet_type=ec2.SubnetType.PUBLIC,)] 
                     
            )
     
       # Creëer een SG voor de webserver
        sg_webserver = ec2.SecurityGroup(self,"sgWebServer", 
                                         vpc = vpc_app,
                                         description = "sg_webserver vanuit CDK",
                                         allow_all_outbound=True,
                                         disable_inline_rules=False,
                                                                                 
                                        )
        sg_webserver.add_ingress_rule(ec2.Peer.ipv4('10.20.20.0/24'), ec2.Port.tcp(22), "SSH toegang voor de adminServer")
        
     
        # Creëer een webserver binnen "app-prd-vpc" die draait op Windows         
        app_server = ec2.Instance(self, "app_server", 
                                  vpc = vpc_app, 
                                  instance_type = ec2.InstanceType('t3a.micro'),
                                  machine_image = ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
                                  security_group = sg_webserver
        )
        # webserver moet via http en https toegankelijk zijn 
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Wereldwijd toegankelijk")
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Wereldwijd toegankelijk")
        
        
        
        
        # Creëer een VPC voor de Management server        
        vpc_admin_server = ec2.Vpc(self, "management-prd-vpc", 
                            nat_gateways = 0,
                            max_azs = 2,
                            ip_addresses = ec2.IpAddresses.cidr("10.20.20.0/24")
                                     
                                                          )
        
        # Creëer een SG voor de admin-server          
        sg_admin_server = ec2.SecurityGroup(self,"sgAdminServer", 
                                         vpc = vpc_admin_server,
                                         description = "sg_admin_server vanuit CDK",
                                         allow_all_outbound=True,
                                         disable_inline_rules=False,
                                    )
        sg_admin_server.add_ingress_rule(ec2.Peer.ipv4('0.0.0.0/0'), ec2.Port.tcp(22), "SSH toegang naar de adminServer van overal") #dit voor nu, aangezien ik niet weer wat de ip-adressen zijn. 

        
        # Creëer een vpc-peering connection in je infrastructuur         
        Cloud_Peering = ec2.CfnVPCPeeringConnection(self, "De_Gewenste_Peering_der_Clouds",
         peer_vpc_id="management-prd-vpc",
        vpc_id="app-prd-vpc",
         )   
             
        # Creëer een management-server binnen de VPC management-prd-vpc, deze zal werken op Linux        
        # Creëer een backup systeem in AWS voor het bedrijf         
        # Implementeer KMS in je infrastructuur         
        # IAM gebruiken in je infrastructuur
        
        # Creëer een ACL voor de admin-server
        # Creëer een ACL voor de app-server      
        
         
                                  
                                  
        
                      





