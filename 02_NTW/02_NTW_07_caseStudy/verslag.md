# [Onderwerp]
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
[Plaats hier de bronnen die je hebt gebruikt.]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

```mermaid
flowchart LR

subgraph Office
  WS1(Workstation 1)
  WS2(Workstation 2)
  WS3(Workstation 3)
  WS4(Workstation 4)
  WS5(Workstation 5)
  Printer
  AD(Active Directory Server)
  FS(File Server)
end

subgraph Internet
  ISP((ISP))
end

subgraph Web
  Firewall
  WebServer(Web Server)
  DB(Database Server)
end

subgraph Network
  Switch1
  Switch2
  WAP1((Wireless Access Point 1))
  WAP2((Wireless Access Point 2))
end

subgraph Monitoring
  NMS(Network Monitoring)
end

ISP --> Firewall
Firewall --> WebServer
WebServer --> DB
Firewall --> Switch1
Firewall --> Switch2
Switch1 --> WS1
Switch1 --> WS2
Switch1 --> WS3
Switch2 --> WS4
Switch2 --> WS5
Switch2 --> Printer
Switch2 --> AD
Switch2 --> FS
Switch1 --> WAP1
Switch2 --> WAP2
NMS --> Switch1
NMS --> Switch2
NMS --> Firewall
```