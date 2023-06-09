# Cron jobs
[Geef een korte beschrijving van het onderwerp]

## Key-terms
**crontab**

## Opdracht
### Gebruikte bronnen
[Plaats hier de bronnen die je hebt gebruikt.]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

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
