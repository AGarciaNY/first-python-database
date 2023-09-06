from flask import Blueprint, render_template, redirect, request
from my_package.my_module import dataBaseConnect

scoreDB = Blueprint("scoreDB", __name__)

@scoreDB.route("/")
def index():
    connectDB = dataBaseConnect()
    cur = connectDB.cursor()
    cur.execute("""SELECT * FROM person""".format(id))

    data = cur.fetchall()
    cur.close()
    connectDB.close()

    return data

@scoreDB.route("/hometwo")
def indexTwo():
    return "hello world two"

@scoreDB.route("/hometwo/<name>")
def indexThree(name):
    return "hello world two" + name