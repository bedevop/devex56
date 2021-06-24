from datetime import datetime

import requests

print(datetime.now())

url = 'https://github.com'
response = requests.get(url)
if response.status_code == 200:
    print('responded ok')

