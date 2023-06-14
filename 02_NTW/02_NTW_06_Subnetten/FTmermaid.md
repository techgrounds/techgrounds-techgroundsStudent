```mermaid
graph LR;

subgraph Main Network
    subnet11(11.0.0.0 - 11.0.0.255<br/>CIDR: 11.0.0.0/24)
end;

subgraph Private Subnet 1
    subnet1(11.0.0.1 - 11.0.0.30<br/>CIDR: 11.0.0.0/27<br/>Available Hosts: 11.0.0.1 - 11.0.0.30<br/>Gateway: Not required)
end;

subgraph Private Subnet 2
    subnet2(11.0.0.32 - 11.0.0.63<br/>CIDR: 11.0.0.32/27<br/>Available Hosts: 11.0.0.33 - 11.0.0.62<br/>Gateway: NAT Gateway)
end;

subgraph Public Subnet
    subnetPublic(11.0.0.64 - 11.0.0.71<br/>CIDR: 11.0.0.64/29<br/>Available Hosts: 11.0.0.65 - 11.0.0.70<br/>Gateway: Internet Gateway)
end;

subnet11 --> subnet1;
subnet11 --> subnet2;
subnet11 --> subnetPublic;
