from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.valoracion import Valoracion as ValoracionModel

#LIBROS_DATA = {
#    1: {"titulo": "Libro 1", "autor": "Autor 1", "valoracion": None, "comentario": None},
#    2: {"titulo": "Libro 2", "autor": "Autor 2", "valoracion": 4.5, "comentario": "Buen libro"}
#}

class Valoracion(Resource):
    def get(self):
        valoraciones = db.session.query(ValoracionModel).all()
        return jsonify([valoracion.to_json() for valoracion in valoraciones])
    def post(self):

        valoraciones = ValoracionModel.from_json(request.get_json())
        db.session.add(valoraciones)
        db.session.commit()
        return valoraciones.to_json(), 201
    
        #user = request.get_json()
        #id = int(max(LIBROS_DATA.keys())) + 1
        #LIBROS_DATA[id] = user
        #return LIBROS_DATA[id], 201
