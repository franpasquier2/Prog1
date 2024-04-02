from flask_restful import Resource
from flask import request

LIBROS_DATA = {
    1: {"titulo": "Libro 1", "autor": "Autor 1", "valoracion": None, "comentario": None},
    2: {"titulo": "Libro 2", "autor": "Autor 2", "valoracion": 4.5, "comentario": "Buen libro"}
}

COMENTARIOS = {
    1: {"titulo": "Libro 1", "autor": "Autor 1", "valoracion": None, "comentario": None},
    2: {"titulo": "Libro 2", "autor": "Autor 2", "valoracion": 4.5, "comentario": "Buen libro"}}


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

# Clase para el recurso de Configuración
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
    

# Recurso para agregar y obtener valoraciones de libros
class Valoracion(Resource):
    def post(self):
        user = request.get_json()
        id = int(max(LIBROS_DATA.keys())) + 1
        LIBROS_DATA[id] = user
        return LIBROS_DATA[id], 201

    def get(self):
        return LIBROS_DATA

# Recurso para agregar y obtener comentarios de libros
class Comentarios(Resource):
    def get(self):
        return COMENTARIOS
    
    def post(self):
        user = request.get_json()
        id = int(max(LIBROS_DATA.keys())) + 1
        COMENTARIOS[id] = user
        return COMENTARIOS[id], 201
