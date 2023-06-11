# Bash scripten


## Key-terms
**PATH variable**  
**variable**  
To assign a variable, use '='. To read the variable's value, use '$' followed by the variable name.

## Opdracht
### Gebruikte bronnen
[Plaats hier de bronnen die je hebt gebruikt.]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
1.1. Uitgevoerd met behulp van 'mkdir' invoer. 
1.2. Eerst heb ik bepaald wat voor een configuratiebestand ik moet veranderen aan de hand van de door mijn gebruikte shell. Dit ging door:
```
$ echo $SHELL
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
uit te voeren. Hierdoor kwam ik in Nano en daar heb ik 
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
chmod +x montage_apache.sh
````
en via 
```
./montage_apache.sh
````
om [dit](./01_04_snip.PNG) resultaat te verkrijgen. 

2.1. Met nano command het bestand numbers_game gemaakt. Daarin schreef ik:
```
#!/bin/bash

# Generate random number between 1 and 10
random_number=$((RANDOM % 10 + 1))

# Append the random number to a text file
echo "$random_number" >> numbers.txt

# Print the random number
echo "Random number generated: $random_number"
```
Dit hierna uitgevoerd door middel van 

```
chmod +x numbers_game
```
en 
```
./numbers_game
```
Dit leverde een tekstbestand op dat steeds werd aangevuld met random getallen. Tot mijn onsteltenis kwam ik erachter het bestand niet eindigde op .sh. Gelukkig kan je bestandsnamen wijzigen. Het volgende heb ik laten uitvoeren:

```
$ mv numbers_game numbers_game.sh
```
Nu eindigt het document op .sh, wat duidelijker is, overwegende het feit dat het bestand effectief een script ís. Ook na de naamsverandering is dat trouwens nog een feit, gezien de bestandsnaam nog steeds in de kleur van een script wordt weergeven in de terminal. Tot slot had de hint uit de opdracht mij al enigzins duidelijk gemaakt dat het praktisch niet fout was dat mijn script niet op .sh eindigde. Dit hint luidde namelijk: "although there are no file extensions in Linux, it’s easier for humans to understand if you end your script names with ‘.sh’."

3.1. Dit gedeelte kan weer worden begonnen met het openen van een script. In dit geval genaamd: munt_gooien.sh. 

De inhoud van het script is: 
```
#!/bin/bash

# Genereer een willekeurig nummer tussen 1 en 10.
willekeurig_nummer=$((RANDOM % 10 + 1))

# Is het nummer hoger dan 5?
if [ "$willekeurig_nummer" -gt 5 ]; then
    echo "$willekeurig_nummer" >> bingo.txt
else
    echo "Jammer, probeer nogmaals." >> bingo.txt
fi
````

Nog een paar opmerkingen over het bovenstaande. Het command RANDOM % zorgt ervoor dat 



