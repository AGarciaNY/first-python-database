from flask import Blueprint, render_template, redirect, request
from my_package.my_module import dataBaseConnect

HWDP = Blueprint("hellow_world", __name__)

@HWDP.route("/")
def index():
    connectDB = dataBaseConnect()
    cur = connectDB.cursor()
    cur.execute("""SELECT * FROM person""".format(id))

    data = cur.fetchall()
    cur.close()
    connectDB.close()

    return data

@HWDP.route("/hometwo")
def indexTwo():
    return "hello world two"

@HWDP.route("/hometwo/<name>")
def indexThree(name):
    return "hello world two" + name