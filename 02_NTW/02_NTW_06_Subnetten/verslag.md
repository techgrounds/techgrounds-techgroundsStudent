# Subnetten


## Key-terms
**NAT**  
Deze afkorting staat voor Netwrok adress translation.  NAT is een technologie die IP-adressen vertaalt tussen verschillende netwerken om meerdere apparaten in een lokaal netwerk via één extern IP-adres verbinding te laten maken met het internet.
**NAT-gateway**  
Een NAT-gateway is een beheerde service in de cloud die IP-adresvertaling mogelijk maakt tussen een virtuele privécloud (VPC) en het internet.
**bit**  
kleinste eenheid van informatie. Het kan een 1 of een 0 zijn. 8 bits vormen samen 1  
**byte**  
**subnet mask / prefix**  
Dit instrument definieert, als we het hebben over een ip-adres, hoeveel bits deel uitmaken van het netwerkadres en hoeveel bits daarnaast louter voor de host gereserveerd zijn. 

## Opdracht
### Gebruikte bronnen
<https://tech-lib.nl/subnetmasker/>  
<https://www.cisco.com/c/nl_nl/support/docs/ip/routing-information-protocol-rip/13788-3.html>  
<https://dnsmadeeasy.com/support/subnet>----->ezelsbrug voor subnet-masken. 


### Resultaat
Voor de netwerkarchitectuur kunnen we uitgaan van het schema hieronder: 

```mermaid
graph LR;

style subnet11 fill:#87CEEB,stroke:#000000,stroke-width:2px;
style subnetPublic fill:#90EE90,stroke:#000000,stroke-width:2px;

subgraph Main Network
    style subnet11 fill:#87CEEB,stroke:#000000,stroke-width:2px;
    subnet11(11.0.0.0 - 11.0.0.255<br/>CIDR: 11.0.0.0/24);
    
    subgraph Private Subnet 1
        style subnet1 fill:#800020,stroke:#000000,stroke-width:2px;
        class subnet1Text fill:#FFFFFF,stroke:none,font-weight:bold;
        subnet1(11.0.0.1 - 11.0.0.30<br/>CIDR: 11.0.0.0/27<br/>Available Hosts: 11.0.0.1 - 11.0.0.30<br/>Gateway: Not required);
    end
    
    subgraph Private Subnet 2
        style subnet2 fill:#800020,stroke:#000000,stroke-width:2px;
        class subnet2Text fill:#FFFFFF,stroke:none,font-weight:bold;
        subnet2(11.0.0.32 - 11.0.0.63<br/>CIDR: 11.0.0.32/27<br/>Available Hosts: 11.0.0.33 - 11.0.0.62);
        gateway(NAT Gateway)
        class gatewayText fill:#000000,stroke:none,font-weight:bold;
    end
    
    subgraph Public Subnet
        style subnetPublic fill:#90EE90,stroke:#000000,stroke-width:2px;
        subnetPublic(11.0.0.64 - 11.0.0.71<br/>CIDR: 11.0.0.64/29<br/>Available Hosts: 11.0.0.65 - 11.0.0.70);
        internetGateway((Internet Gateway))
        class internetGatewayText fill:#000000,stroke:none,font-weight:bold;
    end
    
    


end;


```


*Uitleg van getekende schema*  
Voor de totale opdracht zijn 62 private hosts nodig. De subnet mask van de hoordverbinding kan dus als volgt worden weergeven: 0.0.0.0/24. De hoofdverbinding heb ik voor de vlotte afhandeling van deze opdracht zélf vastgesteld en wel op 11.0.0.0/24. Aan de hand van het schema valt vast te stellen hoe de IP-adressen verder verdeeld zijn. Om te begrijpen wat voor ranges er i.c. gebruikt worden kan het volgende plaatje van dienst zijn:  
![ranges_IP](./Knipsels/RangeVerdeling.PNG)

Ik heb nog een afbeelding gegenereerd met behulp van de applicatie van diagrams.net. Deze afbeelding zal ik hieronder posten ter afsluiting van deze opdracht en om hopelijk de gebruikte architectuur nog duidelijker te krijgen:  

![Eind_Knipsel](./Knipsels/architectuur.drawio.png)
