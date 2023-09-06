from flask import Blueprint, render_template, redirect, request
from my_package.my_module import dataBaseConnect
from cryptography.fernet import Fernet

ACDB = Blueprint("aaccount", __name__)

@ACDB.route("/create_account", methods=["POST"])
def index():
    #connect to database
    connectDB = dataBaseConnect()
    cur = connectDB.cursor()

    #get data from user
    data = request.get_json() 
    user_name = data["user_name"] 
    user_email = data["user_email"] 
    user_password = bytes(data["user_password"],"utf-8")
    print(user_password)
    #encript user password
    key = "lv5h10h7TWqnFW7P0NaHIt2-6UVzjW9AEeLQ8i1MeOA="
    fernet = Fernet(key)
    enc_password = fernet.encrypt(user_password)

    # #post user's data to database
    postgres_insert_query = """ INSERT INTO users(user_name, user_email,user_password) VALUES (%s,%s,%s) RETURNING *"""
    record_to_insert = (user_name, user_email, enc_password)
    cur.execute(postgres_insert_query, record_to_insert)

    new_user_data = cur.fetchall()

    # disconnect from database
    connectDB.commit()
    cur.close()
    connectDB.close()

    #send user data
    return new_user_data, 201

@ACDB.route("/login", methods=["POST"])
def indexTwo():
    #connect to databse
    connectDB = dataBaseConnect()
    cur = connectDB.cursor()

    #get user's data
    data = request.get_json() 
    user_name = data["user_name"]
    user_password = data["user_password"]

    #get user's data by user name
    postgres_insert_query = f""" SELECT user_name, user_password from users where user_name = '{user_name}'"""
    cur.execute(postgres_insert_query)
    new_data = cur.fetchall()
    enc_password = new_data[0][1]

    #decripting user's password
    key = "lv5h10h7TWqnFW7P0NaHIt2-6UVzjW9AEeLQ8i1MeOA="
    fernet = Fernet(key)
    print(enc_password,"here++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    dec_password = base64.urlsafe_b64decode(enc_password)


    connectDB.commit()
    cur.close()
    connectDB.close()
    if user_password == dec_password:
        return True
    return new_data

@ACDB.route("/user_search")
def indexThree():
    return "hello world two"
