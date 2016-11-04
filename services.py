#standard library imports

try:
    from urllib.parse import urljoin
except:
    from urllib import urljoin
import requests


BASE_URL = 'http://jsonplaceholder.typicode.com'
#BASE_URL = 'https://booklos.com'
TODOS_URL = urljoin(BASE_URL,'todos')
#TODOS_URL = 'http://jsonplaceholder.typicode.com/todos'
print (TODOS_URL)
def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None
