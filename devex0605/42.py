import requests

url = 'http://127.0.0.1:5001'
e_p = '/whatismyname'
response = requests.get(url + e_p)
print(response)
print(response.text)
response = requests.post(url + e_p)
print(response)
print(response.text)


