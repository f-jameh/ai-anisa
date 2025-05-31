# in the name of God

from netmiko import ConnectHandler

command = 'ifconfig'
key = '/home/farhad/ai-anisa/Session3/privkey'
host = 'ub1.fartakec.local'

device = {
    "device_type": "linux",
    "host": host,
    "username": "farhad",
    "use_keys": True,
    "key_file": key,
    "port": 22,                 # optional
    }

with ConnectHandler(**device) as ssh:
    print(f'connecting to device: {ssh.find_prompt()} ...')           # show propmt of device
    output = ssh.send_command(command)
    print(output)
    
    
            
        
    
    
    
    
    