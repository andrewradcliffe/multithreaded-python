from dotenv import load_dotenv
import os

load_dotenv()
CONN_STR = os.getenv('CONN_STR')

def main():
    print(CONN_STR)

if __name__ == '__main__':
    main()
