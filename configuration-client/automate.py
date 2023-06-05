import os

superUser = True if os.geteuid() == 0 else False

if superUser:
	os.system('touch /etc/systemd/system/test.service')
	with open('/etc/systemd/system/test.service','w') as f:
                f.write('[Unit]')
                f.write('\n')
                f.write('Description=My Boot Script')
                f.write('\n\n')
                f.write('After=network.target\n')
                f.write('[Service]\n')
                f.write('ExecStart=/usr/bin/python3 /HPE-CTY/configuration-client/bootupfile.py')
                f.write('\n\n')
                f.write('[Install]\n')
                f.write('WantedBy=default.target\n\n')
