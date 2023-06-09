# Cron jobs
[Geef een korte beschrijving van het onderwerp]

## Key-terms
**crontab**

## Opdracht
### Gebruikte bronnen
<https://www.transip.nl/knowledgebase/artikel/484-wat-is-een-cronjob-crontab/>

### Ervaren problemen
Een suf probleempje: ik zag een tijdje niet het verschil tussen de letter L en het cijfer 1 in het font gebruikt in Powershell. Dat zorgde voor wat irritatie bij een gedeelte van de opdracht. 

### Resultaat
1. Begonnen met het maken van een script genaamd tijd dateur.sh. Dit instrumentje geplaatst in de directory '/home/vincent_/scripts'.

Hierna heb ik het volgende geplaatst in het onderhavige bestand: 
```
#!/bin/bash

# Stel de huidige tijd en datum vast
huidige_datum=$(date)

# Specificeer de file path in de home directory
file_path="$HOME/logboek.txt"

# De vaststaande zin wordt hier gespecificeerd
vaststaande_zin="Wij leven onderhand op:"

# Stipuleer de huidige tijd en datum in het logboek
echo "$vaststaande_zin $huidige_datum." > "$file_path"
```
Na het bestand via 

```
$ chmod +x dateur
```
executeerbaar te maken, heb ik het daadwerkelijk geëxecuteerd d.m.v.:
```
$ ./dateur.sh
````


Nu wordt het tijd om de proef op de som te nemen? Is er inderdaad sprake van een bestand logboek.txt in de home directory?

Het bestand is aanwezig, echter we worden geconfronteerd met een probleemje. Er ontstaat steeds een nieuw bestand en er wordt níet steeds één nieuwe regel aan hetzelfde bestand gevoegd. Bij het examineren van mijn code zie ik dat ik louter een '>' heb gebruikt en er dus steeds een nieuwe bestand onstaat. Dit maakt dat de juiste inhoud van het dateur.sh-bestand als volgt zal moeten zijn: 
```
#!/bin/bash

# Stel de huidige tijd en datum vast
huidige_datum=$(date)

# Specificeer de file path in de home directory
file_path="$HOME/logboek.txt"

# De vaststaande zin wordt hier gespecificeerd
vaststaande_zin="Wij leven onderhand op:"

# Stipuleer de huidige tijd en datum in het logboek
echo "$vaststaande_zin $huidige_datum." >> "$file_path"
```
Openen we nu het bestand logboek.txt dan zie we inderdaad dat  het aantal zinnen in het bestand gelijk is aan hoe vaak het script dateur.sh gerund is. 



2. Om te beginnen met de opdracht heb ik de crontab geopend. Dit ging zo: 

```
$ crontab -e

```
Nu heb ik ervoor gekozen in nano de crontab te openen. Gezien het feit dat we maar in de eerste week van onze cursus zijn, is mijn crontab nog leeg, los van wat generieke instructies. Deze instructies heb ik eruit gehaald en ik heb in mijn crontab het volgende geplaatst: 

```
* * * * * /bin/bash /home/vincent_/scripts/dateur.sh  
````

Hierbij staat elke asterisk voor een bepaald moment. Zie de bron hierboven weergegeven voor een uitgebreide uitleg. Het komt er kort gezegd op neer dat er voor elk moment een positieve respons is gekozen. Dat zorgt er vervolgens voor dat i.c. dateur.sh elke minuut wordt ingezet. 
Tot slot zullen wij moeten nagaan of het bovenstaande daadwerkelijk aan het plaatsvinden is. Nadat er wat tijd verstreken is, zullen er al een aantal zinnen moeten staan in het bestand logboek.txt. Met de command 
```
cat logboek.txt
````
kunnen we in de terminal de inhoud van het meerbedoelde bestand weergeven. We kunnen afleiden uit de uitvoer in de terminal, [hier](./02_Snip.PNG) afgebeeld, dat de cron job wordt uitgevoerd. 

3. Om deze opdracht uit te voeren scrhijven we een script in capacité.sh. De grondslag voor dit script zal zijn: 

```
#!/bin/bash

# Haal de huidige datum en tijd op
huidige_datum=$(date)

# Haal de beschikbare schijfruimte op
schijf_ruimte=$(df -h / | awk 'NR==2 {print $4}')

# Schrijf de schijfruimte naar het logbestand
log_bestand="/var/log/schijf_ruimte.log"
echo "Datum: $huidige_datum, Beschikbare Schijfruimte: $schijf_ruimte" >> "$log_bestand"
```