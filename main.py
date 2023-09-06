import rsa
import os
from flask import  Flask, request, jsonify
from my_package.my_module import dataBaseConnect

#routs
from DBblueprints.hello_world.hello_world import HWDP
from DBblueprints.account.account import ACDB
from DBblueprints.friend.friend import friendDB
from DBblueprints.score.score import scoreDB

# ras key cript
with open("keyPriv2.pem","rb") as f:
    priveKey = rsa.PrivateKey.load_pkcs1( f.read())
    print(type(priveKey))

with open("keyPub2.pem","rb") as f:
    pubKey = rsa.PublicKey.load_pkcs1( f.read())
    # print(priveKey)
ms = "password"
codeMS = b"5\xf4\x9d\xa4\xbcZ_\xa6p\x8eV\xbd\tj\x02\x10'\x0c\x96\xda[\x08\x00*\x15\xcf\xe9u\x99DV\xd2.L\xd3a\x8d \xc6\x8c\x1b\xed\x9b~z\xd7\x95\xf3xC\xe0;\x1b#e-.3\xf2\xaa+\x1a\xf4\xe1\xcb\x13\x9b\x07AA\xe6\x0e\x1b-4\xe8\x14\xa3[\xf6[\xa1rrs+\xb4y1\xc9\x18\xbc\x80\xd4hV\xc6/\xdaZ'BB%\xaa\xb5y\x93\xe9\x89\x18\x0b\xba\x8d-(\xb9\xf7\xd3\xe4\xde\xe4-\xcc\x92\x06\xe4@"
encMS = rsa.encrypt(ms.encode(),pubKey)
deMS = rsa.decrypt(codeMS,priveKey)
print(deMS) 
print(encMS) 
 
# friend_requests
app = Flask(__name__)

app.register_blueprint(HWDP, url_prefix="/")
app.register_blueprint(ACDB, url_prefix="/account")
app.register_blueprint(friendDB, url_prefix="/friend")
app.register_blueprint(scoreDB, url_prefix="/score")

def setUp():
    conn = dataBaseConnect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTs person(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR);
            """)
    
    cur.execute("""CREATE TABLE IF NOT EXISTs users(
            user_id SERIAL,
            user_name VARCHAR(255) UNIQUE, 
            user_email VARCHAR(255),
            user_password VARCHAR(255)
                );
            """)
#     cur.execute("""INSERT INTO person ( id, name, age, gender) VALUES
#             (1,'steve',21,'m'),
#             (2,'Gab',30,'m'),
#             (3,'Yeni',51,'m');
#             """)
    conn.commit()
    cur.close()
    conn.close()
setUp()

# @app.route("/")
# def home():
#     return "hello world One"



# @app.route("/data/<id>")
# def getData(id):

#     connectDB = dataBaseConnect()
#     cur = connectDB.cursor()
#     cur.execute("""SELECT * FROM person WHERE id = {}""".format(id))

#     data = cur.fetchall()
#     cur.close()
#     connectDB.close()
#     return data


# @app.route("/data-add", methods=["POST"])
# def data_add():
#     connectDB = dataBaseConnect()
#     cur = connectDB.cursor()
     
#     data = request.get_json()
#     print(data["id"], "here_________________()()())()(()()()())")
#     user_id = data["id"]
#     user_name = data["name"]
#     user_age = data["age"]
#     gender = data["gender"]
#     cur.execute("""INSERT INTO person ( id, name, age, gender) VALUES(%s,%s,%s,%s)""",(user_id, user_name, user_age, gender))
#     connectDB.commit()
#     cur.close()
#     connectDB.close()
#     return jsonify(data), 201



if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))