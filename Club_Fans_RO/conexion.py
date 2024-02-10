import sqlite3

class Conexion:
    def __init__(self,querySql,params=[]):
        self.con = sqlite3.connect("data/Registro_Club_Fans_RO.sqlite")
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql, params)