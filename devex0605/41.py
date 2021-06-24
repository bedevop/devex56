import requests

url = 'https://api.github.com/users/avielb/repos'
response = requests.get(url)
print(response)

all_repos = response.json()
for _ in all_repos:
    if 'name' in _.keys():
        print(_['name'])

