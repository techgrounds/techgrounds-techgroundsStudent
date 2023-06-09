# RDS & de Aurora Engine
Het volgende is belangrijk om te onderstrepen. Aurora is eigenlijk een variant van RDS (Relational Database Service) binnen AWS. Het is een specifiek type relationele database-engine dat is ontworpen om compatibiliteit te bieden met MySQL- en PostgreSQL-databases, terwijl het verbeterde prestaties en schaalbaarheid biedt. 


NB Aurora’s I/O-Optimized  is een nieuwe cluster-opslagconfiguratie die voorspelbare prijzen biedt voor alle toepassingen en verbeterde prijs-prestatieverhouding, met tot wel 40% kostenbesparing voor I/O-intensieve toepassingen.
## Key-terms
**RDS**: Deze afkorting staat voor "Relational Database Service".  
**DB**: Deze afkorting staat voor database doorgaans.  
**DB instance**: Dit is een geïsoleerde DB-omgeving die draait in de Cloud.  
**relationele database**: Een relationele database is een type database dat gegevens organiseert en opslaat in tabellen met rijen en kolommen. Het maakt gebruik van gestandaardiseerde relaties tussen de tabellen om gegevens te organiseren en relaties tussen verschillende entiteiten vast te leggen. Dit maakt het mogelijk om complexe en gestructureerde gegevens op een efficiënte manier op te slaan, te beheren en op te vragen. Relationele databases maken gebruik van de SQL (Structured Query Language) voor het beheren en manipuleren van gegevens.  
**Amazon Aurora**: Dit is een onderdeel van Amazon RDS. Het is een relationele database engine. Deze engine van Amazon is te gebruiken met MySQL en PostgreSQL. Overigens, een aurora betekent in het Engels een lichtstraal in de atmosfeer.  
**MySQL**: database engine die ook draait in RDS. Deze engine ondersteunt ook AWS RDS Read Replicas.  
**PostgreSQL**: database engine die ook draait in RDS. Deze engine ondersteunt ook AWS RDS Read. Hoe het ook zij, een engine kan qua naam eindigen op SQL. 



## Opdracht
### Gebruikte bronnen
[User Guide RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)  
[Case Study usage of Aurora](https://aws.amazon.com/solutions/case-studies/reasonlabs-case-study/?did=cr_card&trk=cr_card)
[Second Case Study usage of Aurora](https://aws.amazon.com/solutions/case-studies/talabat-case-study/?did=cr_card&trk=cr_card)
[FAQ voor RDS](https://aws.amazon.com/rds/faqs/)
### Ervaren problemen
Het was listig meteen te begrijpen hoe Aurora zich verhoudt met AWS RDS. Toen ik daadwerkelijk met het creëren van een DB aan de slag ging, ging ik het concept Aurora beter begrijpen. Dit kwam omdat ik Aurora nu kon kiezen als een engine voor mijn database die ik maakte om mee te oefenen. 

### Resultaat
Allereerst begonnen met het creëren van een DB. Daarbij heb ik gekozen voor een Aurora engine, aangezien we in deze opdracht ook met Aurora dienen te werken. Hieronder een screenshot van het geheel: ![Alt text](image.png)  


