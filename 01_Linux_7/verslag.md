# Bash scripten]
[Geef een korte beschrijving van het onderwerp]

## Key-terms
**PATH variable**

## Opdracht
### Gebruikte bronnen
[Plaats hier de bronnen die je hebt gebruikt.]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
1.1. Uitgevoerd met behulp van 'mkdir' invoer. 
1.2. Eerst heb ik bepaald wat voor een configuratiebestand ik moet veranderen aan de hand van de door mijn gebruikte shell. Dit ging door:
```
$ echo $ShELL
````
Hierdoor kwam ik erachter dat ik aan het werk was met de Bash shell. Nu wordt het tijd het configuratiebestand daarvan aan te passen. Dit bestand heb ik zo geopend:
```
$ sudo nano ~/.bashrc$
````
Toen het bestand geopend was heb ik 
```
$ export PATH="/home/vincent_/scripts:$PATH"
````
toegevoegd. 
Hierna heb ik door middel van 
```
$ echo $PATH
```
gezien dat er succesvol mijn folder aan de PATH-variabele was toegevoegd. Zie daarvan [dit](./01_02_Snip.PNG) screenshot.  
1.3. Voor dit component van de opdracht beginnen we eerst met een script maken. i.c. door 
````
$ nano glosseerder.sh
````
uit te veoren. Hierdoor kwam ik in Nano en daar heb ik 
````
#!/bin/bash
echo "Dit is een glosse van de glosseerder" >> /home/vincent_/scripts/de_codi.txt
````
ingevoerd in het bestand. Ik heb dit opgeslagen en heb toen nano afgesloten. Toen ik weer in het terminal heb ik o.b.v. 
````
chmod +x glosseerder.sh
````
gefixt dat het bestand glosseerder.sh uitvoerbaar was. Tot slot heb ik door 
```
./glosseerder.sh
````
uit te voeren geregeld dat er een lijn tekst werd toegevoegd aan het tekstbestand de_codi.txt. Gezien het feit dat dit laatsgenoemde bestand nog niet bestond, zal het dus door het runnen van het script moeten ontstaan. Door 
```
$ ls -l
````
te runnen heb ik gecontroleerd of meerbedoelde tekstbestand bestaat. Warempel, het is geslaagd! Klik om dat met eigen ogen te aanschouwen [hier](./01_03_Snip.PNG).  
1.4.Via nano een script gemaakt dat montage_apache heet. De inhoud van dat script is:
````
#!/bin/bash

# Install httpd package
sudo apt update
sudo apt install -y apache2

# Start and enable httpd
sudo systemctl start apache2
sudo systemctl enable apache2

# Check status of httpd
sudo systemctl status apache2

````
Dit script uitgevoerd via
```
chmod +x setup_httpd.sh
````
en via 
```
./setup_httpd.sh
````
om [dit](./01_04_snip.PNG) resultaat te verkrijgen. 

2.1.


