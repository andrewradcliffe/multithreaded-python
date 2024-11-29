from mongoengine import connect
from main import CONN_STR

def connect_mongo():
    connect(host=CONN_STR)
