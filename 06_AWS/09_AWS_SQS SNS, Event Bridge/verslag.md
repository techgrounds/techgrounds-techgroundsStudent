# SNS, SQS, Event Bridge
In dit verslag zullen meerdere services de revue passeren: SNS, SQS en Event bridge. We beginnen met die laatste.  
Amazon EventBridge is een serverloze service die "events" gebruikt om applicatiecomponenten met elkaar te verbinden, waardoor het voor ontwikkelaars gemakkelijker wordt om schaalbare "event-driven" applicaties te bouwen. Events kunnen voortkomen uit je eigen applicaties, SaaS-applicaties en AWS services. Deze events kunnen dan worden verzonden naar een andere service om gebruikt te worden. Denk hierbij bijvoorbeeld aan een service als AWS lambda.  

Komen we nu bij AWS SQS. Deze afkorting staat voor Simple Queue Service. Het werkt als volgt. "Producers" sturen berichten naar de "SQS queue. Producers kunnen applicaties zijn, microservices en alle AWS-services. De SQS-queue slaat de berichten op. De berichten kunnen vervolgens worden verwerkt door "consumers", als ze daar klaar voor zijn. Consumers kunnen applicaties zijn of verschillende AWS-services. Het volgende plaatje helpt om het concept snel te begrijpen: ![e.g.](image.png)

Nasa gebruikt de SQS-service bijvoorbeeld om inkomende ""jobs" van pipeline processen te ontkoppelen. 

Tot slot bespreken we in de verslag nog SNS. Deze drie letters staan voor Simple Notification Service. 


het volgende plaatje zal hopelijk helpen deze dienst goed te begrijpen: 

Nasa gebruikt de SNS-service bijvoorbeeld om het pipeline proces op gang te brengen als er nieuwe content wordt geüpload. 


## Key-terms
**SaaS**: "Software as a service"  
**ABAC**: "Attribute-based access control"

## Opdracht
### Gebruikte bronnen
[Plaats hier de bronnen die je hebt gebruikt.]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]
