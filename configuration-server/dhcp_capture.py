#!/usr/bin/env python3
"""scapy-dhcp-listener.py

Listen for DHCP packets using scapy to learn when LAN 
hosts request IP addresses from DHCP Servers.

Copyright (C) 2018 Jonathan Cutrer

License Dual MIT, 0BSD

"""

from __future__ import print_function
from scapy.all import *
import time
import sys
import re
import os
import threading

__version__ = "0.0.3"

# Fixup function to extract dhcp_options by key
def get_option(dhcp_options, key):

    must_decode = ['hostname', 'domain', 'vendor_class_id']
    try:
        for i in dhcp_options:
            if i[0] == key:
                # If DHCP Server Returned multiple name servers 
                # return all as comma seperated string.
                if key == 'name_server' and len(i) > 2:
                    return ",".join(i[1:])
                # domain and hostname are binary strings,
                # decode to unicode string before returning
                elif key in must_decode:
                    return i[1].decode()
                else: 
                    return i[1]        
    except:
        pass


def handle_dhcp_packet(packet):

    # Match DHCP discover
    if DHCP in packet and packet[DHCP].options[0][1] == 1:
        print('---')
        print('New DHCP Discover')
        # print(packet.summary())
        # print(ls(packet))
        hostname = get_option(packet[DHCP].options, 'hostname')
        print(f"Host {hostname} ({packet[Ether].src}) asked for an IP")


    # Match DHCP offer
    elif DHCP in packet and packet[DHCP].options[0][1] == 2:
        print('---')
        print('New DHCP Offer')
        # print(packet.summary())
        # print(ls(packet))

        subnet_mask = get_option(packet[DHCP].options, 'subnet_mask')
        lease_time = get_option(packet[DHCP].options, 'lease_time')
        router = get_option(packet[DHCP].options, 'router')
        name_server = get_option(packet[DHCP].options, 'name_server')
        domain = get_option(packet[DHCP].options, 'domain')

        print(f"DHCP Server {packet[IP].src} ({packet[Ether].src}) "
              f"offered {packet[BOOTP].yiaddr}")

        print(f"DHCP Options: subnet_mask: {subnet_mask}, lease_time: "
              f"{lease_time}, router: {router}, name_server: {name_server}, "
              f"domain: {domain}")


    # Match DHCP request
    elif DHCP in packet and packet[DHCP].options[0][1] == 3:
        print('---')
        print('New DHCP Request')
        # print(packet.summary())
        # print(ls(packet))

        requested_addr = get_option(packet[DHCP].options, 'requested_addr')
        hostname = get_option(packet[DHCP].options, 'hostname')
        print(f"Host {hostname} ({packet[Ether].src}) requested {requested_addr}")


    # Match DHCP ack
    elif DHCP in packet and packet[DHCP].options[0][1] == 5:
        print('---')
        print('New DHCP Ack')
        # print(packet.summary())
        # print(ls(packet))

        subnet_mask = get_option(packet[DHCP].options, 'subnet_mask')
        lease_time = get_option(packet[DHCP].options, 'lease_time')
        router = get_option(packet[DHCP].options, 'router')
        name_server = get_option(packet[DHCP].options, 'name_server')

        print(f"DHCP Server {packet[IP].src} ({packet[Ether].src}) "
              f"acked {packet[BOOTP].yiaddr}")

        print(f"DHCP Options: subnet_mask: {subnet_mask}, lease_time: "
              f"{lease_time}, router: {router}, name_server: {name_server}")

    # Match DHCP inform
    elif DHCP in packet and packet[DHCP].options[0][1] == 8:
        print('---')
        print('New DHCP Inform')
        # print(packet.summary())
        # print(ls(packet))

        hostname = get_option(packet[DHCP].options, 'hostname')
        vendor_class_id = get_option(packet[DHCP].options, 'vendor_class_id')

        print(f"DHCP Inform from {packet[IP].src} ({packet[Ether].src}) "
              f"hostname: {hostname}, vendor_class_id: {vendor_class_id}")

    else:
        print('---')
        with open('captured_packet.txt','w') as f:
            sys.stdout = f
            print('Some Other DHCP Packet')
            print(packet.summary())
            print(ls(packet))
        sys.stdout = sys.__stdout__
        
        pattern = r"\bb'[Hh].*,.*,\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3},[0-9a-fA-F]{2}[:\-][0-9a-fA-F]{2}[:\-][0-9a-fA-F]{2}[:\-][0-9a-fA-F]{2}[:\-][0-9a-fA-F]{2}[:\-][0-9a-fA-F]{2}\b"
        f = open('captured_packet.txt','r')
        text = f.read()
        print(text)
        f.close()

        match = re.findall(pattern,text)
        # match = os.popen("tr -d 'b'' {}".format(match)).read()
        print(match)
        with open("devices.csv","a+") as file:
            all_devices_details = file.read()
            if len(all_devices_details) == 0:
                try:
                    captured_device = match[0][2:]
                    print(captured_device,file=file)
                    with open('captured_packet.txt','w') as fb:
                        pass
                    return
                except Exception:
                    pass

            try:
                captured_device = match[0][2:]
                for device_detail in all_devices_details:
                    if captured_device.split(",")[4] not in device_detail:
                        print("New device is added")
                        # file.write(captured_device) or
                        print(captured_device,file=file)
            except Exception:
                pass
        
        # print(match[0][2:])


        with open('captured_packet.txt','w') as fb:
            pass

        os.system("sort devices.csv | uniq > tempdevices.csv")
        os.system("sed '/^$/d' tempdevices.csv > devices.csv")
        # os.system("cat tempdevices.csv > devices.csv")
        os.system("rm tempdevices.csv")
        print(open("devices.csv",'r').read())

    return

if __name__ == "__main__":
    sniff(filter="udp and (port 67 or 68)", prn=handle_dhcp_packet,iface="enp0s3")
