from dotenv import load_dotenv
import os
from db import connect_mongo

load_dotenv()
CONN_STR = os.getenv('CONN_STR')

def main():
    connect_mongo()

if __name__ == '__main__':
    main()
