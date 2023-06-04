import os

superUser = True if os.geteuid() == 0 else False

if superUser:
	os.system('touch /etc/systemd/system/test.service')
        with open('/etc/systemd/system/test.service','w') as f:
                f.write('[Unit]\n')
                f.write('Description=My Boot Script\n')
                f.write('After=network.target\n')
                f.write('[Service]\n')
                f.write('ExecStart=/HPE-CTY/configuration-client/bootupfile.py\n')
                f.write('[Install]\n')
                f.write('WantedBy=default.target\n')
