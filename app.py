import psycopg2
from flask import  Flask, request, jsonify


app = Flask(__name__)

def dataBaseConnect():
    connectDB = psycopg2.connect(host="localhost",
                             dbname="postgres",
                             user="postgres",
                             password="ag",
                             port=5432)
    return connectDB


@app.route("/")
def home():
    connectDB = dataBaseConnect()
    cur = connectDB.cursor()
    cur.execute("""SELECT * FROM person""")
    data = cur.fetchall()
    cur.close()
    connectDB.close()
    return data


@app.route("/data/<id>")
def getData(id):

    connectDB = dataBaseConnect()
    cur = connectDB.cursor()
    cur.execute("""SELECT * FROM person WHERE id = {}""".format(id))

    data = cur.s
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
    app.run(debug=True)