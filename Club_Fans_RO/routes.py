from Club_Fans_RO import app
from flask import render_template,request,redirect,flash
from Club_Fans_RO.models import *
import sqlite3
from Club_Fans_RO.forms import ValidatorForm

def validarFormulario(datosFormulario):
    errores=[]
    if datosFormulario['Nombre'] == "":
        errores.append("El nombre no puede ir vacío")
    if datosFormulario['Apellidos'] == "":
        errores.append("El apellido no puede ir vacío")
    if datosFormulario['Mail'] == "":
        errores.append("El Email no puede ir vacío")
    if datosFormulario['Telefono'] == "" or int(datosFormulario['telefono']) == 0.0:
        errores.append("El Teléfono no puede ir vacío ni tener números decimales")
    


@app.route("/")
def index():
    return render_template("inicio.html")


@app.route("/Biografia")
def biografia():
    return render_template("biografia.html")


@app.route("/Conciertos")
def conciertos():
    return render_template("conciertos.html")


@app.route("/Clubdefans")
def Club_de_Fans():
    return render_template("club_de_fans.html")


@app.route("/Suscripcion")
def suscripcion():
    datos_sql = select_all()
    return render_template("index.html", data=datos_sql)

@app.route("/Contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/new", methods=["GET","POST"])
def create():
    valido = ValidatorForm()

    if request.method == "GET":
        return render_template("create.html", dataForm=valido)

    else: #post
        if valido.validate_on_submit():
            insert([request.form['nombre'],
                request.form['apellidos'],
                request.form['mail'],
                request.form['telefono']
                ])
            flash("¡Inscrito correctamente!")
            return redirect("/Suscripcion")
        else:
            return render_template("create.html", dataForm=valido)


@app.route("//update/<int:id>", methods=["GET","POST"])
def editar(id):
    if request.method == "GET":
        valido = ValidatorForm()
        resultado = select_by(id)

        valido.nombre.data = resultado[1]#nombre
        valido.apellidos.data = resultado[2]#apellidos
        valido.mail.data = resultado[3]#mail
        valido.telefono.data = resultado[4]#telefono
        return render_template("update.html", dataForm=valido, idForm = id )
    else: #post
        valido = ValidatorForm()
        update_by(id,[valido.nombre.data,
                valido.apellidos.data,
                valido.mail.data,
                valido.telefono.data
                ])
        flash("¡Registro actualizado correctamente!")
        return redirect("/Suscripcion")

@app.route("/delete/<int:id>", methods=["GET","POST"])
def borrar(id):
    if request.method == "GET":

        registro = select_by(id)#Selecciona el registro y lo elimina

        return render_template("delete.html", data = registro)

    else: #post
        delete_by(id)
        flash("Movimiento borrado correctamente")
        return redirect("/Suscripcion")


