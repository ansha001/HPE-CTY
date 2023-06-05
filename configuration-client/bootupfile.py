import os
import time

SuperUser = True if os.geteuid()==0 else False


if SuperUser:
	os.system('touch /etc/dhcp/dhclient.conf.bak')
    	#   copy contents of dhclient.conf from /usr/share/doc/dhcp-client/dhclient.conf.example
	os.system('cp /usr/share/doc/dhcp-client/dhclient.conf.example /etc/dhcp/dhclient.conf.bak')
	with open('/etc/dhcp/dhclient.conf.bak','r') as setupfile:
		with open('/etc/dhcp/dhclient.conf','w') as configfile:
			for line in setupfile:
				configfile.write(line)
			from clientDetails import ClientDetails as cd
			cdetails = cd()
			details = cdetails.details
			details = details.replace('"',r'\"')
			details = details.replace("{",r"\{")
			details = details.replace("}",r"\}")
			configfile.write('send vendor-class-identifier "{}";\n'.format(details))

	os.system("dhclient -r")
	time.sleep(3)

#	os.system("systemctl restart NetworkManager")
	os.system("dhclient -v")
