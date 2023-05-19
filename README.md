# Project: Auto-Location of servers in a network

Purpose: To develop a management software/application that can locate the server’s identity and display Server Vendor, Server Model, Server Serial Number and Server IP in a web GUI.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine/s.
### Prerequisites
* A set of systems connected to form a dhcp-network where one of the system acts as a dhcp server and is responsible for assigning ip addresses to the client systems.

For this project, we used virtual machines to setup the DHCP network. If you intend to use VirtualBox for running virtual machines, follow the following steps to configure the initial network:
### Network Set-up
1. On all the machines, navigate to Settings>Network and choose 'Internal-network' as the network adapter.
2. We do not want the ip of the server machine to change thus manually assign ip to the server. 
3. Set the client machines to receive ip-addresses through DHCP.

For more instructions on set-up and configurations, refer respective folders.
### Flow Diagram

![AUTO-LOCATE-SERVERS](https://github.com/ansha001/HPE-CTY/assets/79073575/cebe40cf-a3b3-44db-aa51-c62f1cd01235)
