from mongoengine import DateField, StringField, IntField
from mongoengine.document import Document

class Person(Document):
    forename = StringField()
    surname = StringField()
    email = StringField()
    age = IntField(min_value=0, max_value=100)
    gender = StringField()
    birth_date = DateField()
