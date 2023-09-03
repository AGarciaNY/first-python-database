from flask import Blueprint, render_template, redirect, request

HWBP = Blueprint("hellow_world", __name__)


@HWBP.route("/")
def index():
    return "hello world"

@HWBP.route("/hometwo")
def indexTwo():
    return "hello world two"

@HWBP.route("/hometwo/<name>")
def indexThree(name):
    return "hello world two" + name