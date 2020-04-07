# testing paramiko from https://searchnetworking.techtarget.com/tip/Network-automation-with-Python-Paramiko-Netmiko-and-NAPALM

from time import sleep
import paramiko

HOST = "<ip_address_or_hostname>"

# Create an ssh connection and set terminal length 0
conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(HOST, username="<username>", password="<password>")
router_conn = conn.invoke_shell()
print('Successfully connected to %s' % HOST)
router_conn.send('terminal length 0\n')
sleep(1)        # Wait for the cmd to be sent and processed

# Send the command and wait for it to execute
router_conn.send("show arp\n")
sleep(2)

# Read the output, decode into UTF-8 (ASCII) text, and print
print(router_conn.recv(5000).decode("utf-8"))