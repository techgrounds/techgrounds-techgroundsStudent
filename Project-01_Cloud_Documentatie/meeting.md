# POM 

## Vragen & antwoorden
Q: Wat voor bedrijf zijn jullie en in welke regio's zijn jullie actief?  
A: 

Q: Wat zijn de eisen voor jullie instances?  
A: 

Q: Hoe willen jullie je webserver geinstalleerd hebben?  
A:

Q: Hebben jullie iemand die, nadat alles uitgezet is, de omgeving kan beheren?
A: 

Q: Moeten alle subnets public zijn?
A:    

Q: Waarom zijn twee subnets niet gebruikt? Is dat een gevolg van de GI?
A:

Q: Moeten de disks alleen encrypted zijn at rest of moet de data in transit m.b.t. de disks ook versleuteld zijn?
A:


Q: Enig idee hoe je wil omgaan met toename van traffic?  
A:

Q: Willen jullie gebruik maken van een ASG in dit kader? 
A:   

Q: Hoe zit dat m.b.t. een ALB?  
A: 
Q: Waarom is je management server in een andere region dan je webserver?    
A: 

Q: Waarvoor willen jullie KMS gaan gebruiken?  
A:

Q: Wat doen jullie nu qua backups?   
A: 

Q: RTO in gedachte? RPO mag dus variabel zijn?  
A: 

Q: Wil je van AMI's ook snapshots hebben?   
A: 

Q:Gebruiken jullie S3 alleen voor de PostDeploymentScripts?  
A:   


Q: Hebben jullie altijd VPC-peering connection gebruikt en wat is de reden daarvoor?   
A:

Q: Het lijkt alsof jullie niet gebruik maken van een ACL. Klopt dit?    
A: 

Q: Hoe beschikbaar moeten de postDeploymentScripts zijn?  
A: 

Q: Wat is de uptime voor de app-server?  
A:

Q: wat is de uptime voor de admin-server?  
A:

Q: Hoe wil je de ip-ranges verdelen over de subnets?   
A: 

Q: Wat bedoel je precies met "prd" in je vpc-notatie?  
A:

Q: Waarom is je VPC peering connection tot stand gekomen tussen twee regions en niet tussen de daadwerkelijke VPCs?  
A:  

Q: Dus de admin-server kan alleen bereikbaar zijn via 2 publieke IP-adressen?   
A:

Q: Ik zie dat IAM niet wordt afgebeeld in het diagram. Klopt het dat jullie daar niet mee werken?  
A:

Q: Zijn er bepaalde zaken waar jullie extra tegen beschermd willen worden? DDoS-aanvallen?  
A:

Q: Maken jullie gebruik van databases?  
A:

Q: Welke regions gebruiken jullie nu en welke regions vallen allemaal binnen jullie scope voor gebruik?  
A:

Q: Is er nog een bepaalde manier van versleuteling die toegepast dient te worden?  
A:



Network:
Only 1 NSG per Virtual Network? or do you want to add extra NSG in the future?
IP range for the NSG, /24 seems very big for just one server per NSG.
Is the NSG sufficient as a firewall?
Has the peering full access or are there ports blocked by default?
Why does the client want the webserver in AvailZone 1 and the Mngmntserver in AvailZone 2?

Webserver:
Preferred distribution
Preferred size (compute power)
Disk type, ssd/hdd lrs/grs
What is the required uptime for the webserver
What is the reasoning that the Webserver and Admin server are put in different regions in the diagram attachment? 
Can the webserver and admin server deploy in the same resource group?


Adminserver:
Preferred distribution
Preferred size (compute power)
Disk type, ssd/hdd lrs/grs
What is the required uptime for the webserver



General:
What regions allowed for deployment?
What type of storage for the postDeploymentScripts?
Could the product owner elaborate on the specific goals and benefits the company aims to achieve through this transition to the cloud?



RBAC:
What roles are there in the organization?
What is everyone allowed to do?

