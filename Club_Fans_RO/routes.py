from Club_Fans_RO import app
from flask import render_template,request
from Club_Fans_RO.models import *
from config import *
import sqlite3

def validarFormulario(datosFormulario):
    errores=[]
    if datosFormulario['nombre'] == "":
        errores.append("El nombre no puede ir vacío")
    if datosFormulario['apellidos'] == "":
        errores.append("El apellido no puede ir vacío")
    if datosFormulario['email'] == "":
        errores.append("El Email no puede ir vacío")
    if datosFormulario['telefono'] == "" or int(datosFormulario['telefono']) == 0.0:
        errores.append("El email no puede ir vacío ni tener números decimales")
    


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new", methods=["GET","POST"])
def create():
    valido = ValidatorForm()

    if request.method == "GET":
        return render_template("create.html")

    else: #post
        