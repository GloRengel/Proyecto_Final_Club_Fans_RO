import sqlite3
from Club_Fans_RO.conexion import Conexion

def select_all():
    conectar = Conexion("select * from registro")
    filas = conectar.res.fetchall()
    columnas = conectar.res.description
    lista_registro =[]
 
    for f in filas:
        posicion=0
        registro ={}
        for c in columnas:
            registro[c[0]] = f[posicion]
            posicion +=1

        lista_registro.append(registro) 
    conectar.con.close()

    return lista_registro


def select_by(id):#(Gloria, Rengel, gloria@example.com, 652147841)
    conectarSelectBy = Conexion(f"select * from registro where id={id};")
    regist = conectarSelectBy.res.fetchall()
    conectarSelectBy.con.close()

    return regist[0]


def insert(regist):
    conectarInsert = Conexion("INSERT INTO registro(nombre, apellidos, mail, telefono) VALUES(?, ?, ?,?);",regist)
    conectarInsert.con.commit()#funcion para validar el registro
    conectarInsert.con.close()


def delete_by(id):
    conectDeleteBy= Conexion(f"delete from registro where id={id};")
    conectDeleteBy.con.commit()#funcion para validar borrado
    conectDeleteBy.con.close()
    
def update_by(id,registro):
    conectUpdate = Conexion(f"update registro set nombre=?, apellidos=? , mail=? , telefono=? where id={id};", registro)
    conectUpdate.con.commit()#funcion para editar un registro
    conectUpdate.con.close()
