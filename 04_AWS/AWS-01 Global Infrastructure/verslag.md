# AWS Global Infrastructure
Voor een beter begrip van de AWS Global Infrastructure kunnen we het beste AWS zélf citeren, en wel p. 8 van de AWS Whitepaper (zie het kopje gebruikte bronnen voor een link naar de whitepaper):

*"The AWS Cloud infrastructure is built around AWS Regions and Availability Zones. An AWS Region is a physical location in the world where we have multiple Availability Zones. Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. These Availability Zones offer you the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center. For the latest information on the AWS Cloud Availability Zones and AWS Regions, refer to [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).*


## Key-terms
Zie de vragen van deze opdracht.


## Opdracht
### Gebruikte bronnen  
[Amazon Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)  
[Section Global Infrastructure in the AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html) 
[AWS Whitepaper](./aws-overview-whitepaper.pdf)  
[User Guide Amazon RDS](https://docs.aws.amazon.com/pdfs/AmazonRDS/latest/UserGuide/rds-ug.pdf#Concepts.RegionsAndAvailabilityZones)  
[User Guide Amazon EC2](https://docs.aws.amazon.com/pdfs/AWSEC2/latest/UserGuide/ec2-ug.pdf#using-regions-availability-zones)

### Ervaren problemen

### Resultaat
1.  Een "Availability Zone" is een afgesloten locatie binnen een "AWS region". Zie p. 1252 van de vijfde bron.  
2. Elke "AWS Region" is een afzonderlijk geografisch gebeid.  Zie p. 93 van de vierde bron.
3. Een Edge Location is een site die CloudFront gebruikt om kopieën te cachen van je content. Dit doet Cloudfront om die content sneller bij je gebruikers te krijgen. Zie deze [link](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.edge-location.en.html).  
4. Niet elke regio biedt dezelfde resources aan. Zie p. 1248 van de tweede bron. 
