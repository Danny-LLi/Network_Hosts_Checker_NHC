#!/usr/bin/env python3
from scapy.all import ARP, Ether, srp
import sys
import subprocess

def main():
    if len(sys.argv) < 4 or not sys.argv[3]:
        print("Usage: nhc network_interface ip prefix \n\nexample: nhc wlan0 192.168.1.0 24")
    else:
        net_int = sys.argv[1]
        ip = sys.argv[2]
        prefix = sys.argv[3]

        def discover_hosts(interface):
            print("Scanning")
            # Create an ARP request packet
            arp = ARP(pdst=ip + "/" + prefix)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp

            # Send the packet and capture the response
            try:
                result = srp(packet, timeout=4, iface=interface, verbose=0)[0]
            except Exception as e:
                sys.stderr.write(str(e))
                return []

            # Process the response
            hosts = []
            for sent, received in result:
                hosts.append({'ip': received.psrc, 'mac': received.hwsrc})

            # Return the discovered hosts
            return hosts

        # Redirect errors to /dev/null
        with open('/dev/null', 'w') as dev_null:
            sys.stderr = dev_null
            hosts = discover_hosts(net_int)
            sys.stderr = sys.__stderr__  # Restore stderr

        # Print the discovered hosts
        i = 0
        for host in hosts:
            print("IP_" + str(i) + ":", host['ip'], "\tMAC:", host['mac'])
            i += 1
        print(str(i) + " hosts up")


if __name__ == "__main__":
    main()

