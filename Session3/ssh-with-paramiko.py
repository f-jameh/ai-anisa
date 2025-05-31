# in the name of God

import paramiko

# define variables for ssh
host = 'ub1.fartakec.local'
user = 'farhad'
# password = 'g'
port = 22
priv_key = '/home/farhad/ai-anisa/Session3/privkey'

# define variable for command
command = 'ifconfig'

# create an object for ssh
ssh = paramiko.SSHClient()

# determine authentication policy
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# # give the object of ssh user/pass/host
# ssh.connect(hostname=host, username=user, password=password, port=port)

# give the object of ssh user/host/authentication key
ssh.connect(hostname=host, username=user, key_filename=priv_key)

# connect to host via ssh and run command
stdin, stdout, stderr = ssh.exec_command(command)
output = stdout.read().decode()

print(output)




