# using netmiko for testing SSH connection from https://github.com/ktbyers


from netmiko import ConnectHandler # do not name script as netmiko.py as it will conflict with library
import logging

# Lines 8-9 are optional. It will create a file named 'test.log' in your current directory.
# It will log all reads and writes on the SSH channel.
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")


cisco = {
    'device_type': 'cisco_xe',
    'host': '<ip_address_or_hostname>',
    'username': '<username>',
    'password': '<password>',
}

net_connect = ConnectHandler(**cisco)
net_connect.send_command('send log TEST')
output = net_connect.send_command("show ip int brief | e una")

print(output)

net_connect.disconnect()

'''
Netmiko commonly-used methods:
    net_connect.send_command() - Send command down the channel, return output back (pattern based)
    net_connect.send_command_timing() - Send command down the channel, return output back (timing based)
    net_connect.send_config_set() - Send configuration commands to remote device
    net_connect.send_config_from_file() - Send configuration commands loaded from a file
    net_connect.save_config() - Save the running-config to the startup-config
    net_connect.enable() - Enter enable mode
    net_connect.find_prompt() - Return the current router prompt
    net_connect.commit() - Execute a commit action on Juniper and IOS-XR
    net_connect.disconnect() - Close the connection
    net_connect.write_channel() - Low-level write of the channel
    net_connect.read_channel() - Low-level write of the channel
	
Other used links:
	https://pynet.twb-tech.com/blog/automation/netmiko.html
	https://github.com/ktbyers/netmiko/tree/develop/examples
'''

