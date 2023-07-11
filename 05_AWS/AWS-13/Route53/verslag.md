# Route53
Laten we bij het begin beginnen. Wat is Route53? Amazon Route 53 is een zeer beschikbare en schaalbare webdienst voor het Domain Name System (DNS). Je kunt Route 53 gebruiken om drie belangrijke functies uit te voeren in elke combinatie: domeinregistratie, DNS-routering, en "Health checking". 

Er zijn verschillende manieren om het routen uit te laten voeren. Hieronder een opsomming van de verschillende manieren op te "routen":
• *Simple routing policy* – Gebruik dit voor een enkele bron die een bepaalde functie uitvoert voor jouw domein, bijvoorbeeld een webserver die inhoud levert voor de website example.com. Je kunt eenvoudige routering gebruiken om records aan te maken in een privé gehoste zone.
• *Failover routing policy* – Gebruik dit wanneer je een actief-passieve failover wilt configureren. Je kunt failover routering gebruiken om records aan te maken in een privé gehoste zone.
• *Geolocation routing policy* – Gebruik geolocatie-routering wanneer je verkeer wilt routeren op basis van de locatie van jouw gebruikers. Je kunt geolocatieroutering gebruiken om records aan te maken in een privé gehoste zone.
• *Geoproximity routing policy* – Gebruik dit wanneer je het verkeer wilt routeren op basis van de locatie van je bronnen en, indien gewenst, verkeer wilt verplaatsen van bronnen in de ene locatie naar bronnen in een andere locatie.
• *Latency routing policy* – Gebruik deze policy wanneer je resources in meerdere "Regions" hebt en je "traffic wilt routen naar de "Region" die de beste latency biedt. 
 • *IP-based routing policy* – Maak gebruik van deze policy als je traffic wil routeren op basis van de locatie van de gebruikers en je beschikt over hun IP-adressen. 
 • *Multivalue answer routing policy* – Maak gebruik van deze policy als je wilt dat Route53 DNS-queries met verschillende waarden kan beantwoorden, bijvoorbeeld met verschillende IP-adressen. 
 • *Weighted routing policy* – Maak gebruik van deze policy om traffic naar meerdere resources te routen in de verhoudingen die je zélf opgeeft. Je kan daarnaast Weighted routing policy gebruiken om records te creëren in een Private Hosted Zone. 



Nog een leuk feitje om mee af te sluiten: Route53 is vernoemd naar  poortnummer 53,  aangezien 53 de standaardpoort binnen het TCP/IP protocol is voor DNS-communicatie. 
## Key-terms
**DNS**: Domain Name System  
**record**: Een "record" vertelt het DNS de manier waarop je graag wilt dat je traffic wordt "geroute" naar een specifiek domein en haar sub-domeinen. 
**hosted zone**:  Een "hosted zone" is een houder voor "records". Daarnaast zijn er twee typen "hosted zones": "public" en "private". Een "public hosted zone" bevat "records" die specificeren hoe je verkeer wil routen op het internet. Een "private hosted zone" bevat "records" die specificeren hoe je verkeer wil "routen" binnen je Amazon VPC. 
**VPC**: Virtual Private Cloud. 
**Blue/Green Deployment Methodology**: Blue/green-implementaties bieden releases met vrijwel geen downtime en de mogelijkheid tot terugdraaien. Het fundamentele idee achter een blue/green-implementatie is om het verkeer te verplaatsen tussen twee identieke omgevingen die verschillende versies van jouw applicatie draaien.


## Opdracht
### Gebruikte bronnen
[Developer Guide Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
[Index to supported top-level domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html#registrar-tld-list-index)

### Ervaren problemen


### Resultaat
N.v.t., betreft i.c. een studeerinstructie. 
