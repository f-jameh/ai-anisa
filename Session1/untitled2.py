# in the name of God

import requests

bot_token = '7962962805:AAHYRio1RUFRwesn9q6oECbhg69jyx5RvT4'
caht_id = '194488346'
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
text = 'salam'
payload = {'chat_id': caht_id, 'text': text}

response = requests.post(url, data=payload)

print(response)

