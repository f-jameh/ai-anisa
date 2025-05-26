# in the name of God

# import libraries
from subprocess import run
from time import sleep
time_interval = 2

ip1 = '172.16.1.2'
ip2 = '172.16.1.3'
ip3 = '172.16.1.4'
ip4 = '172.16.1.5'

ip_list = [ip1, ip2, ip3, ip4]


while True:
    for ip in ip_list:
        result = run(['ping', '-c', '1', ip], capture_output=True, text=True)
        print(f'The return code of ip {ip} is {result.returncode}')
        sleep(1)
    sleep(5)
    