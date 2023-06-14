# Subnetten


## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
<https://tech-lib.nl/subnetmasker/>  
<https://www.cisco.com/c/nl_nl/support/docs/ip/routing-information-protocol-rip/13788-3.html>  
<https://dnsmadeeasy.com/support/subnet>----->ezelsbrug voor subnet-masken. 


### Resultaat
Voor de netwerkarchitectuur kunnen we uitgaan van het schema hieronder: 

```mermaid
graph LR;

subgraph Main Network Connection
    style subnet11 fill:#87CEEB,stroke:#000000,stroke-width:2px;
    subnet11(11.0.0.0 - 11.0.0.255<br/>CIDR: 11.0.0.0/24);
end;

subgraph Private Subnet 1
    style subnet1 fill:#800020,stroke:#000000,stroke-width:2px;
    class subnet1Text fill:#FFFFFF,stroke:none,font-weight:bold;
    subnet1(11.0.0.1 - 11.0.0.30<br/>CIDR: 11.0.0.0/27<br/>Available Hosts: 11.0.0.1 - 11.0.0.30<br/>Gateway: Not required);
end;

subgraph Private Subnet 2
    style subnet2 fill:#800020,stroke:#000000,stroke-width:2px;
    class subnet2Text fill:#FFFFFF,stroke:none,font-weight:bold;
    subnet2(11.0.0.32 - 11.0.0.63<br/>CIDR: 11.0.0.32/27<br/>Available Hosts: 11.0.0.33 - 11.0.0.62<br/>Gateway: 11.0.0.63);
end;

subgraph Public Subnet
    style subnetPublic fill:#90EE90,stroke:#000000,stroke-width:2px;
    subnetPublic(11.0.0.64 - 11.0.0.71<br/>CIDR: 11.0.0.64/29<br/>Available Hosts: 11.0.0.65 - 11.0.0.70<br/>Gateway: 11.0.0.71);
end;

subnet11 --> subnet1;
subnet11 --> subnet2;
subnet11 --> subnetPublic;


```


*Uitleg van getekende schema*  
Voor de totale opdracht zijn 62 private hosts nodig. De subnet mask van de hoordverbinding kan dus als volgt worden weergeven: 0.0.0.0/24. De hoofdverbinding heb ik voor de vlotte afhandeling van deze opdracht zélf vastgesteld en wel op 11.0.0.0/24. 