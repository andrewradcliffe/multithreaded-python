from mongoengine import DateField, StringField, IntField
from mongoengine.document import Document

class Person(Document):
    forename = StringField()
    surname = StringField()
    email = StringField()
    age = IntField()
    gender = StringField()
    birth_date = DateField()

    @classmethod
    def create(cls, user):
        person = cls()
        person.forename = user.get('firstName')
        person.surname = user.get('lastName')
        person.email = user.get('email')
        person.gender = user.get('gender')
        person.birth_date = user.get('birthDate')
        return person
