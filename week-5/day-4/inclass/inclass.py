import requests
from requests.api import request
from requests.models import Response
import random
# response = requests.get("http://api.open-notify.org/iss-now.json")

# print(response.status_code)

response = requests.get('https://api.chucknorris.io/jokes/categories' )
if response.status_code == 200:
    categories = response.json()

print(categories)
category = random.choice(categories)
response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
print(response.json()['value'])