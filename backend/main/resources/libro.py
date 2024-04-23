from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.libro import Libro as LibroModel

#LIBROS = {
#    1: {"titulo": "Harry Potter", "autor": "J.K. Rowling", "genero": "Fantasía"},
#    2: {"titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "genero": "Fantasía"}
#}

# Defino el recurso Libro
class Libro(Resource):
    # Obtener un libro por ID
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json()
        #if int(id) in LIBROS:
        #    return LIBROS[int(id)]
        #return "", 404

    # Eliminar un libro por ID
    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return libro.to_json(), 204

        #if int(id) in LIBROS:
        #    del LIBROS[int(id)]
        #    return "", 204
        #return "", 404

    # Modificar un libro por ID
    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json() , 201
        #if int(id) in LIBROS:
        #    libro = LIBROS[int(id)]
        #    data = request.get_json()
        #    libro.update(data)
        #    return "", 201
        #return "", 404

# Colección de libros
class Libros(Resource):
    # Obtener lista de libros
    def get(self):

        libros = db.session.query(LibroModel).all()
        return jsonify([animal.to_json() for animal in libros])
        #return LIBROS

    # Insertar un nuevo libro
    def post(self):
        libros = LibroModel.from_json(request.get_json())
        db.session.add(libros)
        db.session.commit()
        return libros.to_json(), 201
        #libro = request.get_json()
        #id = int(max(LIBROS.keys())) + 1
        #LIBROS[id] = libro
        #return LIBROS[id], 201