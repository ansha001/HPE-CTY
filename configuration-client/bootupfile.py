import os
import time

SuperUser = True if os.geteuid()==0 else False


if SuperUser:
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
	os.system("dhclient -v")
