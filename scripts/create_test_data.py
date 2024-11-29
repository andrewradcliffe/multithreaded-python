from db import connect_mongo
from models.person import Person
import requests

def main():
    res = requests.get('https://dummyjson.com/users')
    users = res.json().get('users')

    for user in users:
        person = Person.create(user=user)
        person.save()

if __name__ == '__main__':
    connect_mongo()
    main()
