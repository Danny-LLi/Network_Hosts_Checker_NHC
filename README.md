# Network_Hosts_Checker_NHC
The Network Host Scanner is a simple Python script that utilizes the Scapy library to scan a network for active hosts. It sends ARP (Address Resolution Protocol) requests to discover hosts within a specified IP range.

## Prerequisites

- Python 3.x
- Scapy library

## Installation

1. Clone the repository:
   ```shell
git clone https://github.com/Danny-LLi/Network_Hosts_Checker_NHC.git
2. Install the required dependencies:
   ```shell
pip install scapy
## Usage
nhc network_interface ip prefix
network_interface: The network interface to use for scanning (e.g., wlan0).
ip: The IP address to scan (e.g., 192.168.1.0).
prefix: The CIDR prefix length (e.g., 24).

Example:
nhc wlan0 192.168.1.0 24
