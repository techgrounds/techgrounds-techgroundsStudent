
# Doel van document
Tijdens het implementeren van het ontwerp zal ik beslissingen maken over o.a. diensten die we gaan gebruiken. In dit document zal ik de overwegingen uitschrijven en de besluiten onderbouwen. Dit document zal ook al mijn assumpties  en verbeteringen bevatten. Voorts zal dit document dienen als basis voor mijn ontwerpdocumentatie. In dit document zal ook input van de PO verwerkt worden. 

# Epic Exploratie

## Overzicht van de eisen van PO
### Alle VM disks moeten encrypted zijn.
We zullen dit project gaan uitvoeren in de AWS-omgeving. Er zal dus niet gewerkt worden met entiteiten die letterlijk "VM-disks" worden genoemd. EC2-Instances zijn de entiteiten waar de besturingssystemen op zullen worden gedraaid. Deze gebruiken als root-volume  een EBS-volume of een instance store volume. Gezien het feit dat EBS-volumes gebruiken kunnen maken van de Amazon EBS-encryptie kunnen we aannemen dat PO op basis van EBS-volumes zal willen werken.  
### De webserver moet dagelijks geback-upt worden. De backups moeten 7 dagen behouden worden.  
Dit moet in AWS te regelen zijn met de AWS-backup. De Huidige gang van zaken bevragen om duidelijk te krijgen in hoeverre al gebruik wordt gemaakt van AWS-backup 

### De webserver moet op een geautomatiseerde manier geïnstalleerd worden.
Om deze eis te implementeren kunnen terugvallen op de methodes we in eerdere projecten gebruikt hebben om op een automatische manier webservers te installeren. Met behulp van User Data in de setup van instances hebben we dit kunnen bereiken op een eenvoudige manier en economische manier. Dit lijkt nu ook de voor de hand liggende optie. 

### De admin-server moet bereikbaar zijn met een publiek IP.
Dit is de default binnen AWS meen ik mij te herinneren. Zo niet, dan kan dat sowieso bij de opstart van de server geregeld worden. 

### De admin-server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis)
Dit kan via firewall settings makkelijk worden bereikt. 

### IP-ranges die worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24
Achterhalen in hoeverre er nog eisen zijn qua ip-ranges in de subnets
### Alle subnets moeten beschermd worden door een firewall op subnet niveau.
Dit kan in AWS geregeld worden door gebruik te maken van ACLs.
### SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin-server.
SSH- en RDP-verbindingen zullen dus niet toegestaan zijn voor elke andere server. Dit is in te stellen als deze andere servers worden gecreëerd. 

## Vragen voor POM
Voor de POM hebben we ook aandachtig het aangedragen diagram bestudeerd. Deze ziet er zo uit:   
![](../00_includes/Project/Schermafbeelding%202023-08-22%20om%2011.57.30.png)

Al het voorgaande overwegende heb ik de volgende vragen:  

Wat zijn de eisen voor jullie instances?  
Moeten alle subnets public zijn?   
Waarom zijn twee subnets niet gebruikt? Is dat een gevolg van de GI? 
Enig idee hoe je wil omgaan met toename van traffic?  
Maken jullie gebruik van een ASG in dit kader?   
Hoe zit dat m.b.t. een ALB?   
Waarom is je management server in een andere region dan je webserver?    
Waarvoor willen jullie KMS gaan gebruiken?  
Wat doen jullie nu qua backups?   
RTO in gedachte? RPO mag dus variabel zijn?  
Wil je van AMI's ook snapshots hebben?   
Wat voor bedrijf zijn jullie en in welke regio's zijn jullie actief?  
Gebruiken jullie S3 alleen voor de PostDeploymentScripts?  
Hebben jullie altijd VPC-peering connection gebruikt en wat is de reden daarvoor?  
Het lijkt alsof jullie niet gebruik maken van een ACL. Klopt dit?   
Hoe beschikbaar moeten de postDeploymentScripts zijn?  
Wat is de uptime voor de app-server?  
wat is de uptime voor de admin-server?  
Hoe wil je de ip-ranges verdelen over de subnets?    
Wat bedoel je precies met "prd" in je vpc-notatie?  
Waarom is je VPC peering connection tot stand gekomen tussen twee regions en niet tussen de daadwerkelijke VPCs?    
Dus de admin-server kan alleen bereikbaar zijn via 2 publieke IP-adressen?   
Ik zie dat IAM niet wordt afgebeeld in het diagram. Klopt het dat jullie daar niet mee werken?  
Zijn er bepaalde zaken waar jullie extra tegen beschermd willen worden? DDoS-aanvallen?  
Maken jullie gebruik van databases?  
Welke regions gebruiken jullie nu en welke regions vallen allemaal binnen jullie scope voor gebruik?  
Is er nog een bepaalde manier van versleuteling die toegepast dient te worden?


## Overzicht aannames van onze kant

## overzicht cloudinfrastructuur en bijbehorende diensten
EC2  
IAM  
KMS  
AWS Backup  
AWS Firewall      
S3  
VPC Peering(?)  
EBS  
Cloudwatch  
Trusted Advisor  
Cloudformation  
Secret Key Manager(?)  
EFS (?)  
AWS Shield (?)  










