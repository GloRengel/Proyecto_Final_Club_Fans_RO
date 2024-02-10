"""
delete
def remove(id):
        if request.method == "GET":

            registro = select_by(id)#Selecciona el registro y lo elimina

            return render_template("delete.html", data = registro)

        else: #post
            delete_by(id)
            flash("Movimiento borrado correctamente")
            return redirect("/")

"""

"""
if request.method == "GET":
        valido = ValidatorForm()
        resultado = select_by(id)

        valido.nombre.data = (resultado[1])#nombre
        valido.apellidos.data = resultado[2]#apellidos
        valido.email.data = resultado[3]#email
        valido.telefono.data = resultado[4]#telefono
        return render_template("update.html", dataForm=valido, idForm = id )
    else: #post
        update_by(id,[valido.nombre.data,
                valido.apellidos.data,
                valido.email.data,
                valido.telefono.data
                ])
        flash("Registro actualizado correctamente")
        return render_template("index.html", dataForm=valido)

"""