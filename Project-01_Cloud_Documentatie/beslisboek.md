# Beslisboek
## Doel van document
Tijdens het implementeren van het ontwerp zal ik beslissingen maken over o.a. diensten die we gaan gebruiken. In dit document zal ik de overwegingen uitschrijven en de besluiten onderbouwen. Dit document zal ook al mijn assumpties en verbeteringen bevatten. Voorts zal dit document dienen als basis voor mijn ontwerpdocumentatie.
## Eisen PO
### Alle VM disks moeten encrypted zijn.
We zullen dit project gaan uitvoeren in de AWS-omgeving. Er zal dus niet gewerkt worden met entiteiten die letterlijk "VM-disks" worden genoemd. EC2-Instances zijn de eniteiten waar de besturingssystemen op zullen worden gedraaid. Deze gebruiken als root-volume  een EBS-volume of een instance store volume. Gezien het feit dat EBS-volumes gebruiken kunnen maken van de Amazon EBS-encryptie kunnen we aannemen dat PO op basis van EBS-volumes zal willen werken. 
### De webserver moet dagelijks gebackupt worden. De backups moeten 7 dagen behouden worden.

### De webserver moet op een geautomatiseerde manier geïnstalleerd worden.
Om deze eis te implementeren kunnen terugvallen op de methodes we in eerdere projecten gebruikt hebben om op een automatische manier webservers te installeren. Met behulp van User Data in de setup van instances hebben we dit kunnen bereiken op een eenvoudige manier en economische manier. Dit lijkt nu ook de voor de hand liggende optie. 

### De admin/management server moet bereikbaar zijn met een publiek IP.
Dit is de default binnen AWS. 

### De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis)
Dit kan via firewall settings makkelijk worden bereikt. 

###
