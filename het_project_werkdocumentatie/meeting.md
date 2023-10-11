# POM 24-08-2023

## Vragen & antwoorden
Q: Wat voor bedrijf zijn jullie en in welke regio's zijn jullie actief?  
A: Synthia / Cynthia, een bedrijf dat actief is in Nederland en heel Europa. 

Q: Could the product owner elaborate on the specific goals and benefits the company aims to achieve through this transition to the cloud?  
A: Betere bereikbaarheid, profiteren van de cloud in de meest brede zin. Denk aan de voordelen die erin zijn gestampt tijdens het CPE. 

Q: Welke rollen zijn er binnen jullie organisatie?  
A: Focus er nu op dat de admin van het bedrijf zijn werk goed kan uitvoeren. 

Q: Wat voor bevoegdheden hebben die bovengenoemde rollen?
A: Er is een admin in house, dus die zal de AWS-omgeving beheren.

Q: Wat zijn de eisen voor jullie instances?  
A: Focus vooral op hoe er wordt verbonden met de instances.  Kijk vooral dus naar de eisen van de PO in de user stories rondom SSH en RDP. 

Q: Hoe willen jullie je webserver geïnstalleerd hebben?   
A: Prijs is de main focus m.b.t. dit punt. Houd het zo goedkoop mogelijk! 

Q: Hebben jullie iemand die, nadat alles uitgezet is, de omgeving kan beheren?  
A: Er is iemand die het beheer op zich neemt. Deze persoon is in dienst bij PO. 

Q: Moeten alle subnets public zijn?  
A:  Er moeten verschillende VPCs zijn in verband met de security. Dat is voor de PO de enige harde eis. 

Q: Moeten de disks alleen encrypted zijn at rest of moet de data in transit m.b.t. de disks ook versleuteld zijn?   
A: Allebei, hoewel er niet veel data in transit zal zijn in deze casus. 


Q: Enig idee hoe je wil omgaan met toename van traffic?    
A: n.v.t., pas bij v1.1.

Q: Willen jullie gebruik maken van een ASG in dit kader?  
A: n.v.t., pas bij v1.1.

Q: Hoe zit dat m.b.t. een ALB?   
A: n.v.t., pas bij v1.1.

Q: Waarom is je management server in een andere region dan je webserver?    
A: Dat is eigenlijk niet een vereiste, op dit punt mag het ontwerp aangepast worden.

Q: Waarvoor willen jullie KMS gaan gebruiken?  
A: Encrypten at rest en in-transit.

Q: Wat doen jullie nu qua backups?   
A: Maakt niet uit, ga uit van de eis zoals omschreven in de opdracht. 

Q: RTO in gedachte? RPO mag dus variabel zijn?  
A: Niet relevant schijnbaar. 

Q: Wil je van AMI's ook snapshots hebben?   
A: niet relevant aangezien de AMI's via je code uitgezet zullen worden. 

Q:Gebruiken jullie S3 alleen voor de PostDeploymentScripts?  
A: En ook voor de bootstraps-scripts. Deze scripts moeten ook versleuteld zijn en louter de admin mag erbij. 


Q: Hebben jullie altijd VPC-peering connection gebruikt en wat is de reden daarvoor?   
A: Wat VPC-peering betreft: probeer de kosten hieromtrent laag te houden. 

Q: Het lijkt alsof jullie niet gebruik maken van een ACL. Klopt dit?    
A: Nee, maar dit wil de PO wel graag. Hier moet bij het ontwerp dus rekening mee gehouden worden. 

Q: Hoe beschikbaar moeten de postDeploymentScripts zijn?  
 A: Alleen de admin. 

Q: Wat is de uptime voor de app-server?  En heb jullie nog eisen rondom de specificaties van deze server?  
A: Kies de meest economische oplossing.

Q: wat is de uptime voor de admin-server?  En heb jullie nog eisen rondom de specificaties van deze server?  
A: Kies de meest economische oplossing. 

Q: Hoe wil je de ip-ranges verdelen over de subnets?   
A:  de IP-ranges zijn gelinkt aan 2 subnets, die weer gelinkt mogen zijn aan de 2 VPCs. 

Q: Wat bedoel je precies met "prd" in je vpc-notatie?  
A: "production"  

Q: Dus de admin-server kan alleen bereikbaar zijn via 2 publieke IP-adressen?   
A: Via het kantoor en het huis van de admin mag er verbonden worden met de admin-server. 

Q: Ik zie dat IAM niet wordt afgebeeld in het diagram. Klopt het dat jullie daar niet mee werken?  
A: Er moet wel met IAM gewerkt worden. Wij moeten de IAM situatie uitzetten voor de PO. 

Q: Zijn er bepaalde zaken waar jullie extra tegen beschermd willen worden? DDoS-aanvallen?  
A: Niet NU. Dit druist ook tegen de low-budget insteek van de PO. 

Q: Maken jullie gebruik van databases?  
A: PDS heeft een database nodig. Dus daarvoor zal een database in het leven geroepen moeten worden.  


Q: Is er nog een bepaalde manier van versleuteling die toegepast dient te worden?  
A: Neen, kies maar zelf. 



Q: Is the NSG sufficient as a firewall?  
A: ACLS zijn nodig. SGs zijn verder bij instances de default en waarschijnlijk moeilijk uit te zetten. 






