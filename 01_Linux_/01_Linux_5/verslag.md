# Bestandsrechten
wie en wat mag wat doen?

## Key-terms
**'chown' command**  
**permissions**  


## Opdracht
1.  Create a text file.
2. Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?
3. Make the file executable by adding the execute permission (x).
4. Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?  
5. Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.
6. Change the group ownership of the file to a different group.


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

5. Bij deze opdracht gaan we gebruik maken van een oude vriend, namelijk de gebruiker 'amice_', die we kennen uit een vorige opdracht. Ik ga proberen hem de nieuwe eigenaar te maken van het bestand opdracht.txt.  Doordat we te maken hebben met een handeling die normaal gesproken louter met de benodigde privileges uitgevoerd kan worden, zal ik mijn invoer starten met sudo. met de 'chwon' command kan men de eigenaar van een bestand veranderen.  Uitgangspunt voor deze opdracht gaat, al het voorgaande in overweging nemende, zijn: 
```
$ sudo chown amice_ opdracht.txt
```
Als we nu weer kijken naar de permissions van het bestand, dan zie we hetgeen [hier](/00_includes/05_05_amice_.PNG) wordt afgebeeld. Met een highlicht heb ik aangegeven dat nu amice_ inderdaad het eigendom verkregen heeft van het bestand. Overigens zie ik inderdaad als ik de inhoud van he bestand probeer te lezen dat dat niet gaat. Zie de volgende input en ouput:
```
vincent_@Nest-vi-De-Windt:~/01_Linux_5$ cat opdracht.txt
cat: opdracht.txt: Permission denied
`````
6. Tijd om het bestand volledig in de heerschappij van de nieuwe eigenaar te brengen door het bestand ook tot zijn groep te laten behoren. Er is namelijk ook een groep genaamd 'amice_'. We kunnen dit doen door aan het antwoord van onderdeel vijf twee punten toe te voegen: door middel van een dubbele punt gaan we wederom nu met het 'chown' command de groep van het bestand veranderen. De invoering ziet er zo uit: 
```
$ sudo chown :amice_ opdracht.txt
```
Hierna onderzoeken we de permissions van het bestandje. Daaruit blijkt hopelijk dat het bestand nu tot de groep amice_ behoort. Welnu, bij de controle van de [data](./05_06_newgr.PNG) blijkt inderdaad dat opdracht.txt nu tot de groep amice_ toebehoort! 


