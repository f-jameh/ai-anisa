# in the name of God

from netmiko import ConnectHandler

hosts_file = '/home/farhad/Desktop/Anisa AI/Session2/ip_list.txt'
command_file = '/home/farhad/Desktop/Anisa AI/Session2/commands.txt'

with open(hosts_file, 'r') as file:
    for line in file:
        ip = line.strip()
        
        device = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": "root",
            "password": "1234",
            "port": 22,                 # optional
            "session_log": f"{ip}.txt"    # optional
            }
        
        with ConnectHandler(**device) as ssh:
            print(f'connecting to device: {ssh.find_prompt()} ...')                               # show propmt of device
    
            outout = ssh.send_config_from_file(command_file)             # run Config commands (in config environment)
            output2 = ssh.send_command('wr')
            
            print()
            print(outout)
            print(output2)
            print()
            
        
    
    
    
    
    