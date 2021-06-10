import sys
import os
import re

content = open("Apache.log").read()

ips = []
msgs = []
ip_len = 0

# Parse the log file and extract all needed information.
for line in content.split('\n'):
    # Search and exctract IP adress
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


# Count des adresses IP unique
ips_dict = {}
for ip in set(ips):
    ips_dict[ip] = ips.count(ip)


# Count des messages unique
msgs_dict = {}
for msg in set(msgs):
    msgs_dict[msg] = msgs.count(msg)

print('nombre d"addresse ip (différente): {ip_len}'.format(ip_len=ip_len))

print("\nAddresse IP les plus frequentes:")
for elt in sorted(ips_dict.items(), key=lambda x:x[1], reverse=True)[:10]:
      print("  - {ip} {count} ".format(ip=elt[0], count=elt[1]))

print("\nStatistique des message:")
for elt in sorted(msgs_dict.items(), key=lambda x:x[1], reverse=True):
      print("  - {msg} {count} ".format(msg=elt[0], count=elt[1]))


