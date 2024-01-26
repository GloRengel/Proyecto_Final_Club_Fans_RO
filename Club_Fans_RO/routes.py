from Club_Fans_RO import app
from flask import render_template,request
from Club_Fans_RO.models import *
from config import *
import sqlite3

@app.route("/")
def index():
    return render_template("index.html")