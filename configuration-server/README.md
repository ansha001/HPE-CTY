## SERVER CONFIGURATION

1. Install the DHCP server package by running the following command in the terminal:
```
sudo yum install dhcp
```
2. Open the DHCP configuration file by running the following command in the terminal:
```
sudo vi /etc/dhcp/dhcpd.conf
```
3. In the configuration file, configure the DHCP server settings according to your requirements. For example:
```
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
}
```
4. Start the DHCP service by running the following command in the terminal:
```
sudo systemctl start dhcpd
```
5. Enable the DHCP service to start automatically at boot time:
```
sudo systemctl enable dhcpd
```
