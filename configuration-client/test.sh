#!/bin/bash

# to make certain modifications in dhclient.conf file after copying, i.e replace interface in alias and lease suitable and comment out the "require subnet-mask, domain-name-servers;"
interface=$(ip -o link show | awk -F': ' '{print $2}' | sed -n '2p')
cp /usr/share/doc/dhclient-4.2.5/dhclient.conf.example /etc/dhcp/dhclient.conf
cat /etc/dhcp/dhclient.conf | sed -i "s/interface \"[^\"]*\";/interface \"$interface\";/g" /etc/dhcp/dhclient.conf | sed -i 's/^\(.*require subnet-mask, domain-name-servers\)/#\1/' /etc/dhcp/dhclient.conf


#appended information in dhclient.conf doesn't reflect on server side for first lease request thus release and re-request is performed
dhclient -r
dhclient -v

#to fetch assigned ip address
addresses=$(ip -4 addr | awk '/inet /{print $2}')
IFS=$'\n' read -rd '' -a address_array <<< "$addresses"

if [ "${#address_array[@]}" -ge 2 ]; then
    # Get the second address from the array and store it in the 'second_address' variable
    ip="${address_array[1]}"
else
    echo "Not enough addresses found."
fi

# Get hardware-specific information
#vendor=$(/usr/sbin/dmidecode -s system-product-name)
#serial=$(/usr/sbin/dmidecode -s system-serial-number)

vendor=`head -n 1 /root/info.txt`
model=`head -n 2 /root/info.txt`
serialno=`head -n 3 /root/info.txt`
# Append the vendor-class-identifier to the dhclient.conf file
echo "send vendor-class-identifier \"$vendor, $model, $serialno, $ip\";" >> /etc/dhcp/dhclient.conf

#echo "send vendor-encapsulated-options\"$serialno\";" >> /etc/dhcp/dhclient.conf
