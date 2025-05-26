# in the name of God

#import libraries
import subprocess

# run command with getoutput
output1 = subprocess.getoutput('ls -alh')

print(output1)

# run Command with run
output2 = subprocess.run('ifconfig')
print(output2)
print(type(output2))

output3 = subprocess.run(['ls', '-a', '-l', '-h', '/home/'], capture_output=True, text=True, timeout=5, shell=True)
print(output3.returncode)
print(output3.stderr)
print(output3.stdout)

# save outout in a file
with open ('outou.txt', 'w') as file:
    outout4 = subprocess.run('ifconfig', shell=True, text=True, stdout=file)
    
# shutdown os (linux)
subprocess.run(['sudo', 'shutdown', 'now'])

# shutdown os (windows)
subprocess.run(['shutdown', '/s', '/t', '0'])





