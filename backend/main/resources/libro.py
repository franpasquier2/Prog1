from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.libro import Libro as LibroModel
from datetime import datetime

# Defino el recurso Libro
class Libro(Resource):
    # Obtener un libro por ID
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json(), 201
        
    # Eliminar un libro por ID
    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return libro.to_json(), 204
    

    # Modificar un libro por ID
    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json() , 201


class Libros(Resource):
    
    def get(self):

        libros = db.session.query(LibroModel).all()
        return jsonify([libro.to_json_complete() for libro in libros])

    def post(self):
        libros = LibroModel.from_json(request.get_json())
        db.session.add(libros)
        db.session.commit()
        return libros.to_json(), 201
  