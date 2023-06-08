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
1.3.
