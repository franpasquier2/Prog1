from flask_restful import Resource
from flask import request

LIBROS_DATA = {
    1: {"titulo": "Libro 1", "autor": "Autor 1", "valoracion": None, "comentario": None},
    2: {"titulo": "Libro 2", "autor": "Autor 2", "valoracion": 4.5, "comentario": "Buen libro"}
}

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
        return LIBROS_DATA
    
    def post(self):
        user = request.get_json()
        id = int(max(LIBROS_DATA.keys())) + 1
        LIBROS_DATA[id] = user
        return LIBROS_DATA[id], 201