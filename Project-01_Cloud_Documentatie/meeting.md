# POM 

## Vragen & antwoorden
Q: Wat voor bedrijf zijn jullie en in welke regio's zijn jullie actief?  
A: 

Q: Could the product owner elaborate on the specific goals and benefits the company aims to achieve through this transition to the cloud?  
A:

Q: Welke rollen zijn er binnen jullie organisatie?  
A:

Q: Wat voor bevoegdheden hebben die bovengenoemde rollen?
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

Q: Wat is de uptime voor de app-server?  En heb jullie nog eisen rondom de specificaties van deze server?
A:

Q: wat is de uptime voor de admin-server?  En heb jullie nog eisen rondom de specificaties van deze server?
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

IP range for the NSG, /24 seems very big for just one server per NSG.
Is the NSG sufficient as a firewall?
Has the peering full access or are there ports blocked by default?


Webserver:
Preferred distribution



Adminserver:
Preferred distribution




