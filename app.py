from flask import Flask, jsonify, request
# jsonify permite convertir un obj de python en un obj json
from markupsafe import escape

# creamos una instancia de la clase Flask
app = Flask(__name__)

#       Generando nuevas rutas
# creamos nuestra ruta para soluc el problema NF
@app.route('/')
def index():
    return 'Index'

@app.route('/ping') # '/ping' ruta de lo que escribo a continuación en el nav
def ping():
    return jsonify({"message": "pong"})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})

# manera de solucionarlo:
# el script se interpreta como una cadena de caract, sin importar lo malicioso que sea el código
@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

# Método permitidos para una consulta
# obs: las pruebas hechas previamente en el nav, el valor por defecto siempre fue GET
# @app.route('/recurso', methods=['GET']) # petición GET a la ruta /recurso
# def get_recursos(): # se ejecuta la función
#     return jsonify({"data": "lista de todos los items de este recurso"})
# devuelve: el objeto que indica la clave "data", como referencia se debería devolver todos los items de ese recurso

# para una conexión a una bd: entraríamos a la columna 'recurso'
# consultamos todos los registros de esa bd, formateamos finalmente para devolver el resultado en return

# GET todos los 'recursos'
@app.route('/recurso', methods=['GET'])
def get_recursos():
    return jsonify({"data": "lista de todos los items de este recurso"}) # sólo un recordatorio representativo

# es aplicable para cada una de las entidades, por ej se puede implementar con /cliente
# cuando hablamos de 'recurso' es un nombre genérico a cualquiera de las entidades que se van
# poder acceder a través de esta api.
# nota: las entidades en el proyecto van a ser: los clientes, las facturas, los servicios que tienen un determinado usuario, los productos
# cada uno de esos está asociado en una forma directa a una tabla de la BD
# POST nuevo 'recurso'
@app.route('/recurso', methods = ['POST'])
def post_recurso():
    print(request.get_json()) # realizo la consulta
    body = request.get_json() # al objeto json lo guardo en la var auxiliar body
    # separamos cada una de las claves, recuperamos los valores de la sig forma:
    name = body["name"] # cada uno de los valores lo trabajo como dic
    modelo = body["modelo"] # " "
    # name = request.get_json()["name"] # accedo al dic
    # modelo = request.get_json()["modelo"] # acc al dic
    # insertar en la BD
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo
    }})

# si quisieramos leer uno en particular
# GET un 'recurso' a través de su id
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id): # lo transmito como parámetro de la función
    # buscar en la BD un registro con ese id
    return jsonify({"recurso":{ # devuelve un obj que tiene la clave recurso
        "name": "nombre correspondiente a ese id",  # y a su vez es un objeto
        "modelo": "modelo correspondiente a ese id"
    }})










if __name__ == '__main__':
    # ejecutamos el método run
    app.run(debug=True, port=5000) # debug=True (prueba en modo desarrollo)
                                    # indicamos en qué puerto queremos ejecutar