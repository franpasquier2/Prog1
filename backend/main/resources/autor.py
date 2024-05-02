from flask import Flask, jsonify, request
from flask_restful import Resource
from .. import db
from main.models.autor import Autor as AutorModel
from datetime import datetime

class Autor(Resource):

    def get(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        return autor.to_json(), 201

    # Eliminar un Autor por ID
    def delete(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        db.session.delete(autor)
        db.session.commit()
        return autor.to_json(), 204

    def put(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            if key == "fecha":
                fecha = datetime.strptime(value, '%d-%m-%Y')
                setattr(autor, key, fecha)
            else: 
                setattr(autor, key, value)
        db.session.add(autor)
        db.session.commit()
        return autor.to_json() , 201

class Autores(Resource):
    # Obtener lista de Autores
    def get(self):

        autores = db.session.query(AutorModel).all()
        return jsonify([autor.to_json() for autor in autores])

        #return AutoreS

    # Insertar un nuevo Autor
    def post(self):
        autores = AutorModel.from_json(request.get_json())
        db.session.add(autores)
        db.session.commit()
        return autores.to_json(), 201