from flask_restful import Resource
from flask import request

COMENTARIOS = {
    1: {"titulo": "Libro 1", "autor": "Autor 1", "valoracion": None, "comentario": None},
    2: {"titulo": "Libro 2", "autor": "Autor 2", "valoracion": 4.5, "comentario": "Buen libro"}}

class Comentarios(Resource):
    def get(self):
        return COMENTARIOS
    
    def post(self):
        user = request.get_json()
        id = int(max(COMENTARIOS.keys())) + 1
        COMENTARIOS[id] = user
        return COMENTARIOS[id], 201