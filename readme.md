# Aplicación de Flask con SQLite, HTML y CSS

Programa hecho en python con el framework flask y SQLite, como parte fron end usamos HTML Y CSS.

# Instalación
- crear un entorno en python y ejecutar el comando
```
pip install -r requirements.txt
```
la libreria utilizada en flask https://flask-wtf.readthedocs.io/en/1.2.x/

# Ejecucion del programa
 -iniciar el servidor de flask
 -en mac: 
  ```export FLASK_APP=main.py```
 -en windows:
  ```set FLASK_APP=main.py```

# Comando para ejecutar el servidor
 ```flask --app main run```

# Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
```flask --app main --debug run```

# Otra opción de ejecución 
Crear un archivo .env y dentro agregar los siguiente:
  ``` FLASK_APP=main.py ```
  ``` FLASK_DEBUG=True ```
y luego poder ejecutar en la terminal el comando:
  ``` flask run ```

# Renombrar el archivo config_template a .config y agregar la siguiente linea
  ```ORIGIN_DATA="data/basededatos.sqlite"```
  ```VERSION="v1.0"```

# Base de datos
Crear tabla para registro de personas con la sentencia del archivo create.sql en DB Browser (SQLite)
