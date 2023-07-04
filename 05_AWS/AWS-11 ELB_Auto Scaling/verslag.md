# Elastic Load Balancing (ELB) & Auto Scaling
ELB en Auto Scaling zijn AWS-services die samenwerken om een schaalbare en veerkrachtige architectuur te bieden voor applicaties. ELB verdeelt inkomend verkeer over meerdere bronnen, terwijl Auto Scaling automatisch de capaciteit van resources aanpast aan de vraag. Door ELB en Auto Scaling te combineren, wordt het verkeer efficiënt verdeeld en kunnen resources automatisch worden aangepast, wat resulteert in betere schaalbaarheid, hoge beschikbaarheid en prestaties voor applicaties.

## Key-terms
**ELB**: Elastic Load Balancing is een beheerbare load balancing-service.  
**Auto Scaling**: Mechanisme om capaciteit van je resources automatisch aan de vraag te laten aanpassen.  
**target**: Instances, onderdeel van een targetgroup, die door de ELB worden gebruikt om verkeer naar toe te leiden.  
**NLB**: Network Load balancer, dit is een type Elastic load balancer, aangeboden binnen AWS.  
**Deprecation**: Deprecation binnen AWS verwijst naar het proces waarbij een AWS-service, functie, API of bron wordt stopgezet of niet langer ondersteund. Het is bedoeld om klanten voldoende tijd te geven om over te stappen naar alternatieve oplossingen voordat de betreffende component definitief wordt uitgefaseerd.

## Opdracht
### Gebruikte bronnen
https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-getting-started.html#getting-started-nlb 
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-getting-started.html#configure-target-group-getting-started



### Ervaren problemen
Doordat ik de 1e dag geen Peers in mijn breakout room had, was het lastiger om te achterhalen of ik gedurende de opdracht op de juiste weg zat. 

### Resultaat
We beginnen allereerst met het lanceren van een instance met de specificaties genoemd in de opdracht: ![](/00_includes/05_AWS/Capture_ontsta_retáblissement.PNG). Deze instance heet dus rétablissement. Hierna creëren we een ALB aan de hand van de aanwijzingen in de opdracht: ![](https://github.com/techgrounds/techgrounds-techgroundsStudent/blob/main/00_includes/05_AWS/Capture_creation_ALB.PNG) 

