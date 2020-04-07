import telnetlib
import time

HOST = "<ip_address_or_hostname>"
tn = telnetlib.Telnet(HOST)


tn.write(b'<username>\n')
tn.write(b'<password>\n')
time.sleep(0.5)

tn.write(b"show ip int br | e una\n")
time.sleep(3)

read = tn.read_very_eager().decode('ascii')
print(read)

ip_addr = open('ip_addresses_list.txt','w') # creates new file
ip_addr.write(read) # writing existing IP Addresses on that device

tn.close()


