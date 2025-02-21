import psycopg2 
import os 
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connection successful")
        conn.close()
    except Exception as e:
        print(e)