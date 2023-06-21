# PKI
PKI (Public Key Infrastructure) is een cryptografisch systeem dat vertrouwelijke communicatie en beveiligde digitale transacties mogelijk maakt door middel van het gebruik van openbare en private sleutels.

## Key-terms
De drie entiteiten die bestaan binnen PKI en ervoor zorgen dat je veilig kunt communiceren over een onveilig netwerk zoals het openbare internet zijn:

**1. Certificaatautoriteit (CA):** De CA is verantwoordelijk voor het uitgeven en valideren van digitale certificaten die de identiteit van entiteiten bevestigen.

**2. Registratieautoriteit (RA):** De RA fungeert als een tussenpersoon tussen de CA en de entiteit die een certificaat aanvraagt, en verifieert de identiteit van de aanvrager.

**3. Gebruiker:** De gebruiker maakt gebruik van de digitale certificaten die zijn uitgegeven door de CA om veilige communicatie mogelijk te maken, inclusief het versleutelen van gegevens en het verifiëren van de identiteit van andere entiteiten.

**X.509**  
Dit is een standaard formaat voor digitale certificaten binnen het kader van PKI, dat informatie bevat zoals de identiteit van een entiteit, de openbare sleutel en de handtekening van de certificerende instantie, en wordt gebruikt voor authenticatie en beveiligde communicatie.

## Opdracht
### Gebruikte bronnen
[PKI white paper](./kpi-keyperplus-whitepaper-0622.pdf)----> algemene white paper m.b.t. PKI.  
Chat GPT---->terminologie

### Ervaren problemen


### Resultaat
hieronder de commands die ik heb ingetikt om een "self-signed-certificate" te maken. 

````
$ openssl genpkey -algorithm RSA -out private.key
````
Bovenstaande input gebruikt om een key te genereren. 

Daarna een certificaat aangemaakt genaamd récépissé.crt door middel van het onderstaande.   
````
openssl req -new -key private.key -x509 -days 40 -out récépissé.crt  
````  
Als wij via de commande cat de inhoud van het bestand récépissé.crt  bekijken zie wij dat het bestand inderdaad een certificaat is. de inhoud van het bestand is namelijk:

![knipsel_récépissé](Knipsel_cat_r%C3%A9c%C3%A9piss%C3%A9.PNG)  


Tot slot het einde van de opdracht afgebeeld in knipsel hieronder.  
![afronding](List%20of%20trusted%20certificate%20roots.PNG)


