import os
import psycopg2

# conn = psycopg2.connect(host="localhost",
#                              dbname="postgres",
#                              user="postgres",
#                              password="ag",
#                              port=5432)

conn = psycopg2.connect(os.environ["DATABASE_URL"])

with conn.cursor() as cur:
    cur.execute("SELECT now()")
    res = cur.fetchall()
    conn.commit()
    print(res)

cur = conn.cursor()

# database code
cur.execute("""CREATE TABLE IF NOT EXISTs person(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
);
            """)

cur.execute("""INSERT INTO person ( id, name, age, gender) VALUES
            (1,'steve',21,'m'),
            (2,'Gab',30,'m'),
            (3,'Yeni',51,'m');
            """)

# cur.execute("""SELECT * FROM person WHERE age < 50;""")

# print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
