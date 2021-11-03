from faker import Faker
from os import write
import json
fake = Faker()

with open('file.json','r') as f:
    family = json.load(f)
for child in family['children']:
    child['favorite_color'] = fake.color()
    for key, value in child.items():
        print(f'my {key} is {value}')

