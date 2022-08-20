from faker import Faker
import requests
import random

for i in range(15):

    generator = Faker(['fr-FR'])

    title = " ".join(generator.words(random.randint(3,4)))
    description = generator.text()

    data = {'title':title , 'description':description , 'author':2}

    request = requests.post('http://127.0.0.1:8000/blog/api/posts/',headers={'Accept':'application/json'},data=data)

    with open('debug.html','w') as file:
        file.write(request.text)

    print(request.status_code)