#!/usr/bin/env python3.4

import re
import subprocess
from urllib.request import urlopen

url = 'http://www.ishadowsocks.com/'
req = urlopen(url)
byte_content = req.read()

# Convert the Bytes to String
content = byte_content.decode('utf-8')

# Get Domains
domains = re.findall('[A-Z]服务器地址:(.*)<', content)

ips = []

# Convert Domain to IP
for domain in domains:    
	cmd = ['host', domain]

	# Store the command result into byte_result
	byte_result = subprocess.check_output(cmd)

	# Convert from bytes to string
	str_result = byte_result.decode('utf-8')

	# Get IP from str_result
	ip = re.findall('has address (.*)\n', str_result)

	ips.append(ip)

print('Already get IP...')

# Get port
ports = re.findall('端口:([0-9]*)', content)

print('Already get port...')

# Get Password
passwds = re.findall('[A-Z]密码:([0-9]*)<', content)

print('Already get Password...')

# Write Shadowsocks infomation to a file 
fout = open("ssinfo.txt",'w')
fout.write('Shadowsocks帐号分享\n\n')
for i in range(3):
	fout.write('*'*40+'\n')
	fout.write('{\n\t"server":'+'"'+ips[i][0]+'",\n')
	fout.write('\t"server_port":'+ports[i]+',\n')
	fout.write('\t"local_port":1080\n')
	fout.write('\t"password":'+'"'+passwds[i]+'",\n')
	fout.write('\t"timeout":600,\n')
	fout.write('\t"method":"aes-256-cfb"\n}\n')
	fout.write('*'*40 + '\n\n')

# Determine if add additional Shadowsocks information
additional = False

# Some additional Shadowsocks
if additional:
	try:
		fin = open('ssadd.txt')
		lines = fin.readlines()
		fin.close()

		for line in lines:
			fout.write(line)
	except FileNotFoundError:
		print('File Not Found')


fout.close()

print('Already write to file...')

# Send Email
subject = 'Shadowsocks帐号分享'
MessageFile = '/root/MyProgram/GetSS/ssinfo.txt'
RecipientsFile = '/home/ryt/site/mysite/templates/MyProgram/GetSS/UserAddr.txt'

#fin = open(RecipientsFile)
#recipients = fin.readlines()
#fin.close()
#
#for recipient in recipients:
#	recipient = recipient.rstrip('\n')
#	print(recipient)
#	cmd = ['/root/MyProgram/GetSS/SendMail.sh',subject,recipient,MessageFile]
#	subprocess.call(cmd)
cmd = ['/root/MyProgram/GetSS/SendMail.sh',subject,RecipientsFile,MessageFile]
subprocess.call(cmd)

# Empty RecipientsFile
cmd = ['sed','-i','/.*/d',RecipientsFile]
subprocess.call(cmd)

print('Empty RecipientsFile Completed...')
