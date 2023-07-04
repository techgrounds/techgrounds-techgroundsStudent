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
We beginnen allereerst met het lanceren van een instance met de specificaties genoemd in de opdracht: ![](/00_includes/05_AWS/Capture_ontsta_retáblissement.PNG) Deze instance heet dus rétablissement. Hierna creëren we een ALB aan de hand van de aanwijzingen in de opdracht: ![](https://github.com/techgrounds/techgrounds-techgroundsStudent/blob/main/00_includes/05_AWS/Capture_creation_ALB.PNG)  
We regelen ook dat de ELB een eigen Security Group heeft. Deze Security Group het ELB SG. De Target Group die gebruikt zal worden i.c. heet LabTargetGroup. Zijn targets zullen door auto scalen worden gecreëerd. Later zal nog een knipsel volgen waaruit het bestaan blijkt van de Target Group. Vervolgens heb ik geen launch configuration gecreëerd, aangezien dit niet meer kan in de AWS-console. In plaats daarvan heb ik een  launch template gemaakt. Deze heb ik zo ingesteld dat hij identiek was aan de server genaamd "rétablissement". Hierna heb ik een Auto Scaling Group gemaakt volgens de odpracht. Nu komen we uit bij het gedeelte van de opdracht waarbij we te weten komen of we alle voorgaande stappen correct hebben genomen, het vierde en laatste onderdeel van deze opdracht. We zien nu inderdaad dat er instances via de  ASG online zijn: ![](/00_includes/05_AWS/Capture_4.1.OnlineInstances.PNG) We zien voorts dat de instances deeluitmaken van de Target Group van de Load Balancer: ![](/00_includes/05_AWS/Capture_4.1.Onderdeelvan.PNG) We zoeken daarna de DNS-naam op van de ELB in de AWS-console. We bezoeken deze in de browser: ![](https://github.com/techgrounds/techgrounds-techgroundsStudent/blob/main/00_includes/05_AWS/Capture_4.2.BezoekDNSN_ELB.PNG)  
We kunnen nu een loadtest doen via deze website: ![](/00_includes/05_AWS/Capture_AccessOfServerbyDNS.PNG)  
In de EC2-dashboard zien we nu dat er door de loadtest nuinstances bijkomen: ![](00_includes/05_AWS/Capture_Load_Test.PNG) Dit zien we ook terug bij de target van de Target Group van de ALB: ![](/00_includes/05_AWS/Capture_TargetsOfLabTargetGroup4ELB.PNG)  
Ten slotte zien we dat, nu de loadtest voorbij is, de ASG 2 instances heeft gestopt en getermineerd: ![](/00_includes/05_AWS/Capture_na_de_load_test.PNG)


