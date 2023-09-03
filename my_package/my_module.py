import os
import psycopg2

def dataBaseConnect():
    conn = False
    if os.getenv("DATABASE_URL", default = False) :
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
    else:
        conn = psycopg2.connect(host="localhost",
                             dbname="postgres",
                             user="postgres",
                             password="ag",
                             port=5432)
    
    return conn