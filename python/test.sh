#!/bin/bash
#sudo timeout 10s tcpdump -i ens160 port 67 or port 68 -vvv -s 1500 -l | tee -a /home/surajserver/Downloads/hpe/dhcp.log
grep "Vendor-Class" /root/dhcp.log|cut -d ":" -f 2 | tr -d '"' | tee -a /root/HPE/python/temp.csv
sort /root/HPE/python/temp.csv|uniq|tee /root/HPE/devices.csv