from flask import Flask

app = Flask(__name__,instance_relative_config=True)

app.config.from_object("config")

ORIGIN_DATA = "data/Registro_Club_Fans_RO.sqlite"

from Club_Fans_RO.routes import *