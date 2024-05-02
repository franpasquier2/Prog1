from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.valoracion import Valoracion as ValoracionModel

class Valoracion(Resource):
    def get(self):
        valoraciones = db.session.query(ValoracionModel).all()
        return jsonify([valoracion.to_json() for valoracion in valoraciones])
    
    def post(self):
        valoraciones = ValoracionModel.from_json(request.get_json())
        db.session.add(valoraciones)
        db.session.commit()
        return valoraciones.to_json(), 201