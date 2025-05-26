# in the name of God

from netmiko import ConnectHandler


device1 = {
    "device_type": "cisco_ios",
    "host": "172.16.1.2",
    "username": "root",
    "password": "1234",
    "port": 22,                 # optional
    "session_log": "log.txt"    # optional
    
    }

device2 = {
    "device_type": "cisco_ios",
    "host": "172.16.1.3",
    "username": "root",
    "password": "1234",
    "port": 22,                 # optional
    "session_log": "log.txt"    # optional
    
    }
device3 = {
    "device_type": "cisco_ios",
    "host": "172.16.1.4",
    "username": "root",
    "password": "1234",
    "port": 22,                 # optional
    "session_log": "log.txt"    # optional
    
    }
device4 = {
    "device_type": "cisco_ios",
    "host": "172.16.1.5",
    "username": "root",
    "password": "1234",
    "port": 22,                 # optional
    "session_log": "log.txt"    # optional
    
    }
device_list = [device1, device2, device3, device4]


for device in device_list:
    
    with ConnectHandler(**device) as ssh:
        print(ssh.find_prompt())                # show propmt of device
        backup = ssh.send_command('show run')   # run show commands in device (in basic environment)
        print(backup)
        
        outout = ssh.send_config_set('int loopback 1')                   # run Config commands (in config environment)
        
        ssh.send_command('wr')
        
        print()
        print(outout)
        print()
        
    
    
    
    
    
    