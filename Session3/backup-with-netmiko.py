# in the name of God

from netmiko import ConnectHandler
import datetime

hosts_file = '/home/farhad/ai-anisa/Session3/ip_list.txt'
command = 'show startup-config'

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
            backupname = '/home/farhad/Desktop/backup/' + ssh.find_prompt().strip('#') + '_' + str(datetime.date.today()) + '.txt'
            output = ssh.send_command(command)
            
            with open(backupname, 'w') as file:
                file.write(output)
            print("backup hase been saved to ", backupname)
            
            
            
        
    
    
    
    
    