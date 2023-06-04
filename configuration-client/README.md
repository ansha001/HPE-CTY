## CLIENT CONFIGURATION

On boot up of client machine, first install dhclient package, by running the following command:
```
sudo yum install dhclient
```
### Steps to enable script file test.sh to run on boot:

1. Copy the script file test.sh to a suitable location/ create the file at given location.
```
sudo cp myscript.sh /usr/local/bin/
```

2. Set Permissions: Make the script executable by running the following command:
```
sudo chmod +x /usr/local/bin/myscript.sh
```

3. Create a Systemd Service: Create a systemd service unit file to define the script and its dependencies. In CentOS, these files are typically stored in the /etc/systemd/system/ directory. Use a text editor to create a file, such as test.service, with the following content:
```
[Unit]
Description=My Boot Script
After=network.target

[Service]
ExecStart=/usr/local/bin/test.sh

[Install]
WantedBy=default.target
```

4. Enable the Service:
```
sudo systemctl enable myscript.service
```

5. Reboot the System: To test if the script runs on boot
```
reboot
```

### The info.txt file is assumed to have hardware information for the device ( already appended to it using respective server OS specific commands)
