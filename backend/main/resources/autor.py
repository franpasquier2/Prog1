from flask import Flask, jsonify, request
from flask_restful import Resource
from .. import db
from main.models.autor import Autor as AutorModel
from datetime import datetime

#AUTORES = {
#    1: {'nombre': 'Juan Carlos Nieto'},
#    2: {'nombre': 'María Isabel de las Nieves'},
#    3: {'nombre': 'Luis Alberto Ramírez'}
#}

class Autor(Resource):

    def get(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        return autor.to_json()
    #    if int(id) in AutoreS:
    #       return AutoreS[int(id)]
    #    return '', 404

    # Eliminar un Autor por ID
    def delete(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        db.session.delete(autor)
        db.session.commit()
        return autor.to_json(), 204
        #if int(id) in AutoreS:
        #    del AutoreS[int(id)]
        #    return '', 204
        #return '', 404

    # Modificar un Autor por ID
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
        #if int(id) in AutoreS:
        #    Autor = AutoreS[int(id)]
        #    data = request.get_json()
        #    Autor.update(data)
        #    return '', 201
        #return '', 404

# Colección de Autores
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