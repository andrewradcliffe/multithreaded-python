import time
from datetime import date
from models.person import Person
from mongoengine import connect
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

def add_age(people):
    for person in people:
        today = date.today()
        person.age = today.year - person.birth_date.year - \
            ((today.month, today.day) < 
            (person.birth_date.month, person.birth_date.day))
        person.save()

def add_age_singular(person):
    today = date.today()
    person.age = today.year - person.birth_date.year - \
        ((today.month, today.day) < 
        (person.birth_date.month, person.birth_date.day))
    person.save()

def cleanup(people):
    for person in people:
        person.age = None
        person.save()

def init_db():
    connect(
            db='multithreading',
            host='localhost',
            port=27017,
            maxPoolSize=cpu_count() + 4,
    )

def main():
    init_db()
    people = Person.objects.filter({})

    start = time.time()
    add_age(people)
    print(f'Current method: {time.time() - start} seconds')

    cleanup(people)

    start = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(add_age_singular, list(people))
    print(f'Multiprocessing method: {time.time() - start} seconds')

if __name__ == '__main__':
    main()
