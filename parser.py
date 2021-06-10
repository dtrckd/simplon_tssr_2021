import sys
import os
import re

content = '''
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 06:07:20 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Thu Jun 09 07:11:21 2005] [error] [client 204.100.200.22] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 12:08:57 2005] [error] [client 207.203.80.15] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 12:17:49 2005] [error] [client 216.68.171.39] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 12:48:10 2005] [error] [client 24.158.204.7] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 13:59:36 2005] [error] [client 216.85.154.124] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 14:22:15 2005] [error] [client 219.136.165.149] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 14:40:51 2005] [error] [client 218.114.142.11] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 15:06:08 2005] [error] [client 211.74.182.199] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 16:31:58 2005] [error] [client 218.61.75.217] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 17:04:03 2005] [error] [client 12.32.56.253] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 18:55:10 2005] [error] [client 24.159.188.244] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 18:56:23 2005] [error] [client 222.76.16.61] Directory index forbidden by rule: /var/www/html/
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
[Thu Jun 09 19:23:31 2005] [error] [client 81.199.21.119] File does not exist: /var/www/html/sumthin
'''


ips = []
msgs = []
ip_len = 0
for line in content.split('\n'):
    # search and exctract IP adress
    pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    match = re.search(pattern, line)
    if match != None:
        ip = match.group()
        if ip not in ips:
            ip_len += 1
        ips.append(ip)

    # search and exctract Log Message adress
    pattern = r"\[[a-z]+\]"
    match = re.search(pattern, line)
    if match != None:
        msg = match.group()
        msgs.append(msg[1:-1])


print('nombre d"addresse ip (différente): {ip_len}'.format(ip_len=ip_len))

ips_dict = {}
for ip in set(ips):
    ips_dict[ip] = ips.count(ip)


msgs_dict = {}
for msg in set(msgs):
    msgs_dict[msg] = msgs.count(msg)

print("Addresse les plus frequentes:")
for elt in sorted(ips_dict.items(), key=lambda x:x[1], reverse=True)[:10]:
      print("  - {ip} {count} ".format(ip=elt[0], count=elt[1]))

print("Statistique des message:")
print("Addresse les plus frequentes:")
for elt in sorted(msgs_dict.items(), key=lambda x:x[1], reverse=True):
      print("  - {msg} {count} ".format(msg=elt[0], count=elt[1]))


