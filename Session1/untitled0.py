# in the name of God

### Import libraries
import hashlib
import time
import subprocess
import requests


### define variable
file_path = '/home/farhad/python-class-test'
real_hash = '0c1d60a4882b2f984ca85785d3c572795583abd2'

# send message with telegram
bot_token = '7962962805:AAHYRio1RUFRwesn9q6oECbhg69jyx5RvT4'
caht_id = '194488346'
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
text = f'the file {file_path} is changed'

payload = {'chat_id': caht_id, 'text': text}

numbers = ['+989122758150', '+981234567890', '+8439274598278092']
# print(calculated_hash)

# create an infinitive loop to check hash 
while True:
    
    # open file in binary format
    file= open(file_path, 'rb').read()

    # hash the file
    calculated_hash = hashlib.sha1(file).hexdigest()
    
    if calculated_hash == real_hash:
        print('everything is ok')
    else:
        print(f'Danger!!!! the file {file_path} is changed!!!')
        subprocess.run("vlc /home/farhad/alarm2.mp3", text=True, shell=True)
        for number in numbers:
            subprocess.run(["ssh", "-p", "8022", "u0_a403@10.10.10.249", f"termux-sms-send -n {number} '{file_path}'"], capture_output=True, text=True)
        response = requests.post(url, data=payload)

    time.sleep(5)
    
    




