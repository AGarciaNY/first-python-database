import os
import psycopg2
from flask import  Flask, request, jsonify

from DBblueprints.hello_world.hello_world import HWBP

app = Flask(__name__)
app.register_blueprint(HWBP, url_prefix="/hello")
# acount.setbackEnd(app)
def dataBaseConnect():
    # conn = psycopg2.connect(os.environ["DATABASE_URL"])
    conn = False
    # os.environ.getenv
    # os.getenv("DATABASE_URL", default = False)
    # print(os.environ["DATABASE_URL"],"here Iam __________________")
    if os.getenv("DATABASE_URL", default = False) :
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
    else:
        conn = psycopg2.connect(host="localhost",
                             dbname="postgres",
                             user="postgres",
                             password="ag",
                             port=5432)
    
    return conn
def setUp():
    
    conn = dataBaseConnect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTs person(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR);
            """)
    cur.execute("""INSERT INTO person ( id, name, age, gender) VALUES
            (1,'steve',21,'m'),
            (2,'Gab',30,'m'),
            (3,'Yeni',51,'m');
            """)
    conn.commit()
    cur.close()
    conn.close()
# setUp()

@app.route("/")
def home():
    return "hello world One"



@app.route("/data/<id>")
def getData(id):

    connectDB = dataBaseConnect()
    cur = connectDB.cursor()
    cur.execute("""SELECT * FROM person WHERE id = {}""".format(id))

    data = cur.fetchall()
    cur.close()
    connectDB.close()
    return data


@app.route("/data-add", methods=["POST"])
def data_add():
    connectDB = dataBaseConnect()
    cur = connectDB.cursor()
     
    data = request.get_json()
    print(data["id"], "here_________________()()())()(()()()())")
    user_id = data["id"]
    user_name = data["name"]
    user_age = data["age"]
    gender = data["gender"]
    cur.execute("""INSERT INTO person ( id, name, age, gender) VALUES(%s,%s,%s,%s)""",(user_id, user_name, user_age, gender))
    connectDB.commit()
    cur.close()
    connectDB.close()
    return jsonify(data), 201



if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))