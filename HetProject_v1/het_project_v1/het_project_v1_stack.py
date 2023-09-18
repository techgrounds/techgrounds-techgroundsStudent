import aws_cdk as cdk
from aws_cdk import (
    Stack,
    CfnOutput,
    Duration,
    aws_ec2 as ec2,
    aws_s3 as s3, 
    aws_kms as kms,
    aws_events as events, 
    aws_backup as backup,
    CfnTag,
    aws_iam as iam
)
from constructs import Construct

class HetProjectV1Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        
        # Maak gebruik van IAM in je infrastructuur 
        Instance_Admin = iam.Role(self,"deInstance-Admin",
                             assumed_by = iam.ServicePrincipal("ec2.amazonaws.com"),
                             description = "Admin_spray voor onze beheerserver", 
                             role_name = "Admin_spray_voor_ec2"
        )
        
        Instance_Admin.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
        )
        
        gerant = iam.Role (self, "deGerant",
                          assumed_by = iam.ArnPrincipal("arn:aws:iam::042831144970:user/consommateur"), 
                          description = "Admin_zalf voor YT zodat alle mogelijke problemen kunnen worden aangepakt",
                          role_name = "Admin_zalf"
        )
        
        gerant.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AdministratorAccess')
        )

        
        
        # Implementeer KMS in je infrastructuur 
        de_loper = kms.Key(self, "Loper",
            enable_key_rotation = True, 
            enabled = True, 
            alias = "de_ware_loper"           
                           
        )
        
        
        #   Maak een s3-bucket die encrypted is met meerbedoelde KMS-sleutel 
        deEmmer = s3.Bucket(self, "VersleuteldeEmmer",
        bucket_name = "s3-bucket4scripts",
        access_control = s3.BucketAccessControl.PRIVATE,
        encryption = s3.BucketEncryption.KMS,
        versioned = True,
        block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
        encryption_key = de_loper,
        removal_policy = cdk.RemovalPolicy.DESTROY
        )
        assert (deEmmer.encryption_key == de_loper)

       
       # Creëer een VPC voor de webserver
        vpc_app = ec2.Vpc(self, id = "app-prd-vpc", 
                      nat_gateways = 0,
                      max_azs = 2,
                      ip_addresses = ec2.IpAddresses.cidr("10.10.10.0/24"),
                      vpc_name = "VPClouterVoorDeApp",
                      subnet_configuration = [ec2.SubnetConfiguration(name="Publiek_SN_app",subnet_type=ec2.SubnetType.PUBLIC,)] 
                     
        )
     
       # Creëer een SG voor de webserver 
        sg_webserver = ec2.SecurityGroup(self,"sgWebServer", 
                                         vpc = vpc_app,
                                         description = "sg_webserver vanuit CDK",
                                         allow_all_outbound = True,
                                         disable_inline_rules = False,
                                                                                 
        )
        sg_webserver.add_ingress_rule(ec2.Peer.ipv4('10.20.20.0/24'), ec2.Port.tcp(22), "SSH toegang voor de adminServer")
        sg_webserver.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Wereldwijd toegankelijk")
        sg_webserver.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Wereldwijd toegankelijk")
        sg_webserver.connections.allow_from(ec2.Peer.ipv4('10.20.20.0/24'), ec2.Port.tcp(22), "SSH toegang voor de adminServer")
        sg_webserver.add_egress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "HTTPS wereldwijd toegankelijk tweede optie"
        )
        
     
       # user data definiëren 
        eenvoud_UD = ec2.UserData.for_linux( shebang =  "#!/bin/bash")
        eenvoud_UD.add_commands ( "yum -y install httpd",
                                    "systemctl enable httpd",
                                        "systemctl start httpd",
                                         """echo '<html><h1>L.S., Dit is wat plain text om mijn server wat body te geven, 
                                         hoewel dit gek genoeg niet de body behelst</h1>
                                         <b1> Ik wou dat ik de header was, zodat ik meer body kon geven aan dit alles <b1>                                         
                                         </html>' > /var/www/html/index.html"""
                 
        )                                  
        
         # Creëer wat key-pair zodat er veilig via een SSH-verbinding verbonden kan worden
        sleutelpaar_app = ec2.CfnKeyPair(self, "Sleutelpaar_app_voor_SSH",
                key_name= "sleutelpaar_app",
                key_type = "rsa",
                key_format = "pem",
                tags= [CfnTag(
                    key="sleutels_vd_app",
                    value="sausje safety"
                )]
        )
                 
     
        # Creëer een webserver binnen "app-prd-vpc" die draait op linux en voeg user_data in voor website        
        app_server = ec2.Instance(self, "app_server", 
                                  vpc = vpc_app, 
                                  instance_type = ec2.InstanceType("t3a.micro"),
                                  machine_image = ec2.MachineImage.latest_amazon_linux(
                                    generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2), 
                                  security_group = sg_webserver,
                                  user_data = eenvoud_UD,
                                  key_name =  sleutelpaar_app.key_name,
                                  block_devices =  [ec2.BlockDevice(
                                        device_name= "/dev/sdh",
                                        volume= ec2.BlockDeviceVolume.ebs(8, 
                                        encrypted = True, 
                                        delete_on_termination = True
                                        
                                        )                             
                                    )
                                    ]
                                                                         
                                                                               
        )

       
        
        # webserver moet via http en https toegankelijk zijn en via ssh vanaf de beheerserver
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Wereldwijd toegankelijk")
        app_server.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Wereldwijd toegankelijk")
        app_server.connections.allow_from(ec2.Peer.ipv4('10.20.20.0/24'), ec2.Port.tcp(22), "SSH toegang voor de adminServer")
        
        
        
        
        # Creëer een VPC voor de Management server        
        vpc_admin_server = ec2.Vpc(self, "management-prd-vpc", 
                            nat_gateways = 0,
                            max_azs = 2,
                            ip_addresses = ec2.IpAddresses.cidr("10.20.20.0/24"),
                            subnet_configuration = [ec2.SubnetConfiguration(name="Publiek_SN_Admin",subnet_type = ec2.SubnetType.PUBLIC,)]                            
                            
        )  
          
         # Creëer een SG voor de admin-server          
        sg_admin_server = ec2.SecurityGroup(self,"sgAdminServer", 
                                         vpc = vpc_admin_server,
                                         description = "sg admin_server vanuit CDK",
                                         allow_all_outbound = True,
                                         disable_inline_rules = False,
        )
        sg_admin_server.add_ingress_rule(ec2.Peer.ipv4('86.87.153.240/32'), ec2.Port.tcp(3389), "RDP toegang naar de admin_Server voor de admin") 

        
        # Creëer een vpc-peering connection in je infrastructuur         
        Cloud_Peering = ec2.CfnVPCPeeringConnection(self, "De_Gewenste_Peering_der_Clouds",
         peer_vpc_id = vpc_app.vpc_id,
        vpc_id = vpc_admin_server.vpc_id
        )   
        
        # Creëer een route voor de subnetten van je beheerserver via je VPC-peering naar je webserver
        admin_juiste_route = ec2.CfnRoute(self, "De_route_voor_de_admin",
                                      route_table_id = vpc_admin_server.public_subnets[0].route_table.route_table_id, 
                                      vpc_peering_connection_id = Cloud_Peering.attr_id,
                                      destination_cidr_block = "10.10.10.0/24", 
                                      
        )        
        admin_juiste_route2 = ec2.CfnRoute(self, "De_route_voor_de_admin_2",
                                      route_table_id = vpc_admin_server.public_subnets[1].route_table.route_table_id, 
                                      vpc_peering_connection_id = Cloud_Peering.attr_id,
                                      destination_cidr_block = "10.10.10.0/24", 
                                      
        )
        
        # Creëer een route voor de subnetten van je webserver via je VPC-peering naar je beheerserver
        route_nd_beheerserver = ec2.CfnRoute(self, "route_naar_BS_voor_SN1",
                                             route_table_id = vpc_app.public_subnets[0].route_table.route_table_id, 
                                             vpc_peering_connection_id = Cloud_Peering.attr_id,
                                             destination_cidr_block = "10.20.20.0/24"
        )
        route_nd_beheerserver2 = ec2.CfnRoute(self, "route_naar_BS_voor_SN2",
                                             route_table_id = vpc_app.public_subnets[1].route_table.route_table_id, 
                                             vpc_peering_connection_id = Cloud_Peering.attr_id,
                                             destination_cidr_block = "10.20.20.0/24"
        )
        
        
        # leg de meerbedoelde route vast voor de volledigheid 
        log_admin_route = CfnOutput(self, "log_vd_route", 
                                    value= admin_juiste_route.ref
                                    
        )

        
        # # Kan waarschijnlijk worden verwijderd
        # # Creëer een route van je app_server door je VPC-peering naar je admin-server voor je 1e subnet in app-server 
        # route_tabel_app = ec2.CfnRouteTable(self, "De_enige_wijzer_vd_app",
        #                     vpc_id = vpc_app.vpc_id,
        # )
        
        # app_juiste_route = ec2.CfnRoute(self, "de_route_voor_de_app",
        #                     route_table_id= route_tabel_app.attr_route_table_id,
        #                     destination_cidr_block = "10.20.20.0/24",
        #                     vpc_peering_connection_id = Cloud_Peering.attr_id
        # )
        # # Creëer een route van je app_server door je VPC-peering naar je admin-server voor je 2e subnet in app-server indien nodig 
        
        # Creëer een user_data format voor je management-server
        user_data_management_server = ec2.UserData.for_windows()
        user_data_management_server.add_commands( """<powershell>
                        $adminPassword = "B3h33rd@n"
                        $adminPasswordSecure = ConvertTo-SecureString $adminPassword -AsPlainText -Force
                        Set-LocalUser -Name "Admin" -Password $adminPasswordSecure
                        </powershell>""" 
        )
        
        ## Je hebt maar een sleutel nodig, kijk maar wat je hiermee doet.
        # sleutelpaar_beheerserver = ec2.CfnKeyPair(self, "sleutelpaar_beheerserver_voor_RDP",
        #         key_name= "sleutelpaar_beheerserver",
        #         key_type = "rsa",
        #         key_format = "pem",
        #         description = "toegang tot de beheerserver",
        #         tags= [CfnTag(
        # key="huismeester_bosje",
        # value="WD40_in_a_safety_way"
        #     )]
        # )
        # Creëer een management-server binnen de VPC management-prd-vpc, deze zal werken op Windows en moet via RDP toegankelijk zijn     
        admin_server = ec2.Instance(self, "admin_server", 
                                    instance_type = ec2.InstanceType("t3a.micro"), 
                                    machine_image =  ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
                                    vpc = vpc_admin_server,
                                    security_group = sg_admin_server, 
                                    role = Instance_Admin,
                                    user_data = user_data_management_server,
                                    key_name = sleutelpaar_app.key_name, 
                                    block_devices =  [ec2.BlockDevice(
                                        device_name= "xvdh",
                                        volume= ec2.BlockDeviceVolume.ebs(30, 
                                        encrypted = True, 
                                        delete_on_termination = True
                                        
                                        )                             
                                    )
                                    ]
        )
        # Creëer een backup van de webserver waarbij de backups 7 dagen behouden moeten blijven 
        
        onze_kluis = backup.BackupVault(self, "de_enige_kluis",
                                        backup_vault_name="onze_kluis",
                                        removal_policy=cdk.RemovalPolicy.DESTROY
        )
       
        plan_BU_app = backup.BackupPlan(self, "PDC_BU_app", 
                                        backup_plan_name = "plan_der_dagelijkse_site_backup", 
                                        backup_vault = onze_kluis
        )
        plan_BU_app.add_rule(backup.BackupPlanRule( delete_after = Duration.days(7), 
                                                rule_name = "dagelijkse_back_up",
                                                schedule_expression = events.Schedule.cron(
                                                    minute = "07",
                                                    hour = "01",)
                                            )            
                                    ) 
        
        
        
        plan_BU_app.add_selection(id = "louter_de_app_server", 
                                  resources = [backup.BackupResource.from_construct(app_server)
                                    ] 
        )
                  
                        
    #    Zet je user_data in je nieuw gemaakte bucket en executeer het daarvandaan. Gebruik hierbij Asset. 
                

    
