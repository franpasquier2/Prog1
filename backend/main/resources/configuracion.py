from flask_restful import Resource
from flask import request

CONFIGURACION ={
    1: {
    "nombre_biblioteca": "Biblioteca Central",
    "horario_apertura": "08:00",
    "horario_cierre": "18:00",
    "max_libros_prestamo": 5
},
2: {
    "nombre_biblioteca": "Biblioteca Sur",
    "horario_apertura": "10:00",
    "horario_cierre": "20:00",
    "max_libros_prestamo": 10
}}

class Configuracion(Resource):

    def get(self, id):
        if int(id) in CONFIGURACION:
            return CONFIGURACION[int(id)]
        return '', 404

    def put(self, id):
        if int(id) in CONFIGURACION:
            user = CONFIGURACION[int(id)]
            data = request.get_json()
            user.update(data)
            return "ok",201
        return "", 404
class Configuraciones(Resource):
    # Editar la configuración de la biblioteca (rol: Admin)
    def get(self):
        return CONFIGURACION
    
