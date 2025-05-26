# in the name of God

from netmiko import ConnectHandler

command_list = ['router eigrp 1', 'no auto-summary', 'network 0.0.0.0 0.0.0.0']


ip_list = ['172.16.1.2', '172.16.1.3', '172.16.1.4', '172.16.1.5']


for ip in ip_list:
        
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "root",
        "password": "1234",
        "port": 22,                 # optional
        "session_log": "log.txt"    # optional
        }
    
    with ConnectHandler(**device) as ssh:
        print(f'connecting to device: {ssh.find_prompt()} ...')                               # show propmt of device
        outout = ssh.send_config_set(command_list)             # run Config commands (in config environment)
        output2 = ssh.send_command('wr')
        
        print()
        print(outout)
        print(output2)
        print()
        
    
    
    
    
    
    