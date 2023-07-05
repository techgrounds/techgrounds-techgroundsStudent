# EFS
Amazon Elastic File System verschaft een simpele, schaalbare en elastisch documentatiesysteem om te gebruiken voor algemene workloads binnen AWS en op lokale machines. EFS is compatibel met NFS. Daarnaast is het ook compatibel met alle Linux-based AMIs in EC2. EFS is elastisch, zoals de naam al zegt. Het groeit and krimpt naar gelang de acties van de gebruikers. Belangrijk daarbij is dat gelinkte applicaties door de eerdergenoemde groei en krimp niet worden belemmerd. 

## Key-terms
**EFS**: Elastic File System  
**Resource ID**: Elke Resource binnen EFS heeft een unieke resource identifier (ID)  
**RPC**: Remote Procedure Call. Manier van communicatie tussen clients en servers  
**NFS**: Network File System. Een NFS maakt het mogelijk op een netwerk data op te slaan en daarover te beschikken.  
**POSIX groups**:
**API**: Application Programming Interface.  

## Opdracht
### Gebruikte bronnen
[User Guide voor EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)  
[Demo in Canvas over EFS](https://awsrestart.instructure.com/courses/1943/pages/elastic-file-system-efs-demonstration?module_item_id=1270885)  
[Module in Canvas over EFS](https://awsrestart.vitalsource.com/reader/books/W10D4035V3/pageid/3)  
### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
In het kader van de omgang met Amazon EFS heb ik een EFS gecreëerd: ![](/00_includes/05_AWS/EFS/CaptureCreationEFS.PNG)  
Hierna maken we een EC2 instance om met ons net gemaakte EFS te communiceren. 

