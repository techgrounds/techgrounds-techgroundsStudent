# AWS Global Infrastructure
Voor een beter begrip van de AWS Global Infrastructure kunnen we het beste AWS zélf citeren, en wel p. 8 van de AWS Whitepaper (zie het kopje gebruikte bronnen voor een link naar de whitepaper):

*"The AWS Cloud infrastructure is built around AWS Regions and Availability Zones. An AWS Region is a physical location in the world where we have multiple Availability Zones. Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. These Availability Zones offer you the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center. For the latest information on the AWS Cloud Availability Zones and AWS Regions, refer to [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).*


## Key-terms
**Regions**: Een afzonderlijk geografisch gebied.  
**Availability zone**: Een geïsoleerde locatie binnen een AWS Region.   
**Edge Location**: Een datacenter dat een AWS-dienst gebruikt voor operaties van die specifieke AWS-dienst.  
**RDS**: Een service van AWS. De afkorting staat voor Relational Database Service.  
**PoP**: Deze afkorting staat voor Point of Presence.


## Opdracht
### Gebruikte bronnen  
[Amazon Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)  
[Section Global Infrastructure in the AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html) 
[AWS Whitepaper](./aws-overview-whitepaper.pdf)  
[User Guide Amazon RDS](https://docs.aws.amazon.com/pdfs/AmazonRDS/latest/UserGuide/rds-ug.pdf#Concepts.RegionsAndAvailabilityZones)  
[User Guide Amazon EC2](https://docs.aws.amazon.com/pdfs/AWSEC2/latest/UserGuide/ec2-ug.pdf#using-regions-availability-zones)

### Ervaren problemen
Qua formulering van mijn antwoorden zal ik wat aanpassingen moeten doen. Ik moet mijn antwoord niet te beginnen met het paginanummer van de bron waarin ik mijn antwoord gevonden heb. 

### Resultaat
1. Een "Availability Zone" is een afgesloten locatie binnen een "AWS Region". De code van een Availability Zone wordt gevormd door de code van de AWS Region waar de meerbedoelde Zone bijhoort gevolgd door een letter ter identificatie. Ter illustratie: de code van Availability Zone A in de AWS Region Europe (Paris) is eu-west-3a. Vgl. p. 1252 van de vijfde bron.  
2. Elke "AWS Region" is een afzonderlijk geografisch gebied. Elke region heeft zijn eigen code. De code van de region "Europe (paris)" is bijvoorbeeld eu-west-3. Zie p. 93 van de vierde bron.
3. Een Edge Location is een datacenter. Dit datacenter wordt gebruikt om de operaties van een AWS-service met een zo een laag mogelijke latency bij de klant te krijgen. 
4. Niet elke AWS Region biedt dezelfde resources aan. de keuze voor een Region zal dus afhankelijk zijn van de resources die je nodig hebt. Zie p. 1248 van de laatste bron. 
