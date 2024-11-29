from mongoengine.document import Document
from mongoengine.fields import StringField, IntField
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
CONN_STR = os.getenv('CONN_STR')

def connect_mongo():
    connect(host=CONN_STR)

def main():
    connect_mongo()
    person = Person(forename='John', surname='Doe', age=25)
    person.save()

class Person(Document):
    forename = StringField()
    surname = StringField()
    age = IntField()

if __name__ == '__main__':
    main()
