# Bestandsrechten
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
1.  Create a text file.
2. Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?
3. Make the file executable by adding the execute permission (x).
4. Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?

## Gebruikte bronnen
<https://ubuntu.com/tutorials/command-line-for-beginners#4-creating-folders-and-files>  
ChatGPT


## Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

## Resultaat
1.  Eerst heb ik een nieuwe folder gemaakt voor deze odpracht genaamd 01_linux_5. Dat heb ik gedaan als volgt:
```
 $ mkdir /home/vincent_/01_Linux_5 
 ```
Nadat ik met de cd command naar deze nieuwe map ben gegaan heb ik met het touch command een bestand daar gecreëerd genaamd opdracht. Dat ging zo:
```
$ cd /home/vincent_/01_Linux_5 
````
```
$ touch opdracht.txt
````
Uiteindelijk via het Ls command gezien dat er daadwerkelijk een tekstdocument bestaat in deze map. Zie [dit](/00_includes/05_01_bestand.PNG).  

2.  De informatie die we voor deze vraag nodig hebben kunnen we als verkrijgen: 
```
$ ls -l opdracht.txt
```
Nu verkrijgen we een output die er als volgt uitziet:
```
-rw-rw-r-- 1 vincent_ vincent_ 40 Jun  8 08:00 opdracht.txt
```
Hierbij geeft het eerste daadwerkelijke woord aan dat het bestand eigendom is van vincent_. Het tweede woord is hierbij de aangever van de groep, i.c. vincent_. 
Het feit dat de eerste teken een '-' is betekent dat het een normaal bestand is. Daarna zien we een r en een w. Deze tekens gaan over de permissions van de eigenaar van het bestand.  Deze tekens staan respectievelijk voor 'read' en 'write'. Hierna volgt een '-' Hieruit volgt dat we te maken hebben met een bestand dat niet executeerbaar is door de eigenaar.  
 
 3. Om ons bestand te kunnen executeren heb ik de volgende invoer gebruikt: 
 ```
 $ chmod +x opdracht.txt
 ```
Als we nu weer kijken naar de permissions van het bestand dan zullen we hopelijk zien dat het teken '-' is vervangen door een x. Dit is [i.c](/00_includes/05_03_x.PNG). gelukt.  

4. Bij dit onderdeel van de opdracht kunnen we weer gebruik maken van de 'chmod' command. We zorgen er voor dat alleen wij het bestand kunnen lezen en er in kunnen schrijven door middel van wat volgt: 
````
$ chmod u=rw,go= opdracht.txt
````
Als we dan kijken naar de permissions zien we dat deze veranderd zijn. Een ieder kan dat [hier](/00_includes/05_04_rw.PNG) zien. Duidelijk is dat louter de eigenaar het bestand kan zien en er tekst aan kan toevoegen. 
