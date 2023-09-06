import aws_cdk as cdk
from aws_cdk import (
    Stack,
    CfnOutput,
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

        
        # Maak gebruik van IAM in je infrastructuur 
        Instance_Admin = iam.Role(self,"deInstance-Admin",
                             assumed_by = iam.ServicePrincipal("ec2.amazonaws.com"))
        
        Instance_Admin.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess"))
        
        Gerant = iam.Role(self, "DeGerant",
                          assumed_by = iam.ArnPrincipal("arn:aws:iam::042831144970:user/consommateur"),)
        
        Gerant.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AdministratorAccess'))

        
        
        # Implementeer KMS in je infrastructuur
        de_loper = kms.Key(self, "Loper",
            enable_key_rotation = True, 
            enabled = True,            
                           
                           )
        
        
        #   Maak een s3-bucket die encrypted is met je KMS-sleutel
        deEmmer = s3.Bucket(self, "VersleuteldeEmmer",
        bucket_name = "s3-bucket4scripts",
        access_control = s3.BucketAccessControl.PRIVATE,
        encryption = s3.BucketEncryption.KMS,
        versioned = True,
        block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
        encryption_key = de_loper
        )
        assert (deEmmer.encryption_key == de_loper)

       
       # Creëer een VPC voor de webserver
        vpc_app = ec2.Vpc(self, id = "app-prd-vpc", 
                      nat_gateways = 0,
                      max_azs = 2,
                      ip_addresses = ec2.IpAddresses.cidr("10.10.0.0/24"),
                      subnet_configuration = [ec2.SubnetConfiguration(name="Publiek",subnet_type=ec2.SubnetType.PUBLIC,)] 
                     
        )
     
       # Creëer een SG voor de webserver
        sg_webserver = ec2.SecurityGroup(self,"sgWebServer", 
                                         vpc = vpc_app,
                                         description = "sg_webserver vanuit CDK",
                                         allow_all_outbound = True,
                                         disable_inline_rules = False,
                                                                                 
        )
        sg_webserver.add_ingress_rule(ec2.Peer.ipv4('10.20.20.0/24'), ec2.Port.tcp(22), "SSH toegang voor de adminServer")
        
     
        # Creëer een webserver binnen "app-prd-vpc" die draait op linux         
        app_server = ec2.Instance(self, "app_server", 
                                  vpc = vpc_app, 
                                  instance_type = ec2.InstanceType("t3a.micro"),
                                  machine_image = ec2.MachineImage.latest_amazon_linux(
                                    generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2), 
                                  security_group = sg_webserver,
                                  user_data = ec2.UserData.for_linux(shebang =  """#!/bin/bash
                                    yum -y install httpd
                                    systemctl enable httpd
                                    systemctl start httpd
                                    echo '<html><h1>L.S., MOGE UW TOCHT NAAR DEZE PLAATS VOORSPOEDIG ZIJN GEWEEST </h1></html>' >
                                    /var/www/html/index.html"""
                                    )
                                               
        )
        # webserver moet via http en https toegankelijk zijn 
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Wereldwijd toegankelijk")
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Wereldwijd toegankelijk")
        
        
        
        
        # Creëer een VPC voor de Management server        
        vpc_admin_server = ec2.Vpc(self, "management-prd-vpc", 
                            nat_gateways = 0,
                            max_azs = 2,
                            ip_addresses = ec2.IpAddresses.cidr("10.20.20.0/24"),
                            subnet_configuration = [ec2.SubnetConfiguration(name="Publiek_Admin",subnet_type = ec2.SubnetType.PUBLIC,)]                            
                            
        )
        
        # Creëer een SG voor de admin-server          
        sg_admin_server = ec2.SecurityGroup(self,"sgAdminServer", 
                                         vpc = vpc_admin_server,
                                         description = "sg_admin_server vanuit CDK",
                                         allow_all_outbound = True,
                                         disable_inline_rules = False,
        )
        sg_admin_server.add_ingress_rule(ec2.Peer.ipv4('86.87.153.240/32'), ec2.Port.tcp(22), "SSH toegang naar de adminServer van overal") #dit voor nu, aangezien ik niet weer wat de ip-adressen zijn. 

        
        # Creëer een vpc-peering connection in je infrastructuur         
        Cloud_Peering = ec2.CfnVPCPeeringConnection(self, "De_Gewenste_Peering_der_Clouds",
         peer_vpc_id = "management-prd-vpc",
        vpc_id = "app-prd-vpc",
        )   
             
        # Creëer een management-server binnen de VPC management-prd-vpc, deze zal werken op Linux     
        admin_server = ec2.Instance(self, "admin_server", 
                                    instance_type = ec2.InstanceType("t3a.micro"), 
                                    machine_image = ec2.MachineImage.latest_amazon_linux(
                                        generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2), 
                                    vpc = vpc_admin_server,
                                    security_group = sg_admin_server, 
                                    role = Instance_Admin                                 
        ),
        # Creëer een backup van de webserver waarbij de backups 7 dagen behouden moeten blijven 
        
        plan_BU_app = backup.BackupPlan(self, "plan_der_BU_app"
                                        )
        BU_regel_wekelijks = backup.BackupPlanRule.weekly()
        
        plan_BU_app.add_rule(BU_regel_wekelijks)
        plan_BU_app.add_selection(id = "louter_de_app_server", 
                                  resources = [backup.BackupResource.from_construct(app_server)
                                               ] 
                                  )
        
             
                        
           
        
        
              
        
        # Creëer een ACL voor de admin-server
        # Creëer een ACL voor de app-server      
        
        # scripts in de bucket die je aan het begin hebt gemaakt 
        
      
        
         
                                  
                                  
        
                      





