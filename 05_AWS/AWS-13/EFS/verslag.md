# EFS
Amazon Elastic File System verschaft een simpele, schaalbare en elastisch documentatiesysteem om te gebruiken voor algemene workloads binnen AWS en op lokale machines. EFS is compatibel met NFS. Daarnaast is het ook compatibel met alle Linux-based AMIs in EC2. EFS is elastisch, zoals de naam al zegt. Het groeit and krimpt naar gelang de acties van de gebruikers. Belangrijk daarbij is dat gelinkte applicaties door de eerdergenoemde groei en krimp niet worden belemmerd. 

## Key-terms
**EFS**: Elastic File System  
**Resource ID**: Elke Resource binnen EFS heeft een unieke resource identifier (ID)  
**RPC**: Remote Procedure Call. Manier van communicatie tussen clients en servers  
**NFS**: Network File System. Een NFS maakt het mogelijk op een netwerk data op te slaan en daarover te beschikken.  
**POSIX groups**: Staat voor Portable Operating System Interface. Dit zijn een aantal standaarden die de API bepalen.  
**API**: Application Programming Interface.  
**SG**: Security Group. Hier nog een korte uitleg over SG's in het Engels. In summary, security groups are more instance-centric and operate at the transport layer, while network firewalls are subnet or VPC-centric, operating at the network layer and providing additional features and integrations. Both security groups and network firewalls are important tools for securing your AWS resources, and the choice between them depends on the level of granularity and control you require for your network traffic management.

## Opdracht
### Gebruikte bronnen
[User Guide voor EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)  
[Demo in Canvas over EFS](https://awsrestart.instructure.com/courses/1943/pages/elastic-file-system-efs-demonstration?module_item_id=1270885)  
[Module in Canvas over EFS](https://awsrestart.vitalsource.com/reader/books/W10D4035V3/pageid/3)  
[Website over het mounten van EFS op een EC2-instance](https://computingforgeeks.com/mount-aws-efs-file-system-on-ec2/?expand_article=1)  
### Ervaren problemen
De Security Groups die automatisch werden aangemaakt doordat ik bij het aanmaken van de instance een EFS had gelinkt, zorgden ervoor dat ik niet kon connecteren met mijn instance in eerste instantie. Er was ook nog een tweede probleem. Ik vergat de mount helper via 'amazon-efs utils' te installeren in de 2e instance die ik gebruikte. Hierdoor kon ik in Bash geen gebruik maken van de EFS mount helper. 

### Resultaat
In het kader van de omgang met Amazon EFS heb ik een EFS gecreëerd: ![](/00_includes/05_AWS/EFS/CaptureCreationEFS.PNG)  
Hierna maken we een EC2 instance om met ons net gemaakte EFS te communiceren: ![](/00_includes/05_AWS/EFS/CaptureCreationInstance1.PNG)
Hierna connecteer ik met mijn instance via Powershell. Nadat ik de map efs heb gemaakt, mount ik mijn EFS aan die directory via de command van de EFS mount helper:  
![Alt text](/00_includes/05_AWS/EFS/CaptureMountingEFSinstance1.PNG).  
In mijn instance maak ik verschillende bestanden aan in de map waaraan de EFS gemount is. Hierna delete ik mijn instance en creëer ik een nieuwe instance. In deze nieuwe instance wil ik wederom de EFS mounten en dan zien of ik de eerder gecreëerde bestanden terugvind. In de nieuwe instance mount ik de EFS en ik zie inderdaad mijn eerdere bestanden terug: ![Alt text](/00_includes/05_AWS/EFS/CaptureEFSinInstance2.PNG)  
In de laatste instance heb ik mijn efs gemount via NFS client. Daarvoor gebruikte ik de input die ik kon kopiëren uit de AWS-console voor EFS. Deze luidde als volgt:  
```
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0d703209102453807.efs.eu-central-1.amazonaws.com:/ efs
```
Ik probeerde het mounten eerst te doen via de EFS mount helper, met de volgende command:  
```
sudo mount -t efs -o tls fs-0d703209102453807:/ efs
```
Dit lukte echter niet. Na wat overpeinzingen bedacht ik mij dat ik de mount helper niet op deze nieuwe instance had geïnstalleerd. Ik deed het alsnog via:  
```
sudo yum install -y amazon-efs-utils
```
Hierna zou het wel gelukt zijn om mijn EFS te connecten via de mount helper, ware het niet dat de EFS al geconcerteerd was via de NFS-cliënt: ![Alt text](/00_includes/05_AWS/EFS/CaptureMounHelperUsage.PNG) 
