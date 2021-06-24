import requests
from requests.exceptions import InvalidSchema
from requests.exceptions import ConnectionError

url = ['https://github.com']
url.append('https://github.comz')
url.append('zhttps://github.com')
url.append(None)

for u in url:
    try:
        requests.get(u)
    except InvalidSchema:
        print('schema')
    except ConnectionError:
        print('connection error')
    except BaseException as e:
        print("error" + str(e.args))

print('end')


def get_input_age():
    age = int(input(('Input age')))
    if age < 0:
        raise ValueError('Nagative numer')
    else:
        print('Age is:' + str(age))


try:
    get_input_age()
except ValueError as e:
    print(e.args)
