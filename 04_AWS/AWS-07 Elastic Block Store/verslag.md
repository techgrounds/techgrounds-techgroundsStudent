# Elastic Block Store (EBS)
EBS (Elastic Block Store) is een opslagdienst van Amazon Web Services (AWS) die blokgebaseerde opslagvolumes biedt voor gebruik met EC2-instances. Met EBS kunnen gebruikers persistent gegevens opslaan en koppelen aan hun EC2-instances. Het biedt hoge betrouwbaarheid en prestaties met de mogelijkheid om op verzoek schaalbare opslagvolumes te creëren en aan te passen aan de behoeften van de applicatie. EBS-volumes kunnen worden gebruikt als opstartvolumes voor EC2-instances, om gegevens op te slaan voor databases of om gegevens over te dragen tussen verschillende EC2-instances. EBS ondersteunt functies zoals snapshotting, encryptie en het creëren van geoptimaliseerde volumes voor hogere prestaties.

## Key-terms 
**root volumes**: Dit zal een interne harde schijf op een lokale machine moeten zijn.  
**seperate volume**: Dit zal bijvoorbeeld een externe hard schijf zijn. NB Volumes kunnen opgeschaald worden in AWS, maar ze kunnen niet afgeschaald worden.
**snapshots**: Snapshots in AWS zijn momentopnames van EBS-volumes die worden gebruikt voor back-ups, herstelpunten en het delen van gegevens.


## Opdracht
### Gebruikte bronnen


### Ervaren problemen
In het begin was het onduidelijk voor mij waar ik precies een EBS moet opstarten. 


### Resultaat 
Allereerst heb ik voor deze opdracht een instance en een EBS-volume moeten creëren. Ik zal daarvan hieronder was knipsels laten zien: 
![Ontsta_Machine](./Knipsel_ontstaan_machine.PNG)  
![Ontsta_Volume](./Capture_Ontstaan_Volume.PNG)  
Merk daarbij op dat ik ervoor heb gezorgd dat de instance en het EBS-volume in dezelfde Availibility Zone resideren, namelijk de eu-central-1b Availibity Zone. 
