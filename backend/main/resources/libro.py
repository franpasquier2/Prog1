from flask_restful import Resource
from flask import request

LIBROS = {
    1: {"titulo": "Harry Potter", "autor": "J.K. Rowling", "genero": "Fantasía"},
    2: {"titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "genero": "Fantasía"}
}

# Defino el recurso Libro
class Libro(Resource):
    # Obtener un libro por ID
    def get(self, id):
        if int(id) in LIBROS:
            return LIBROS[int(id)]
        return "", 404

    # Eliminar un libro por ID
    def delete(self, id):
        if int(id) in LIBROS:
            del LIBROS[int(id)]
            return "", 204
        return "", 404

    # Modificar un libro por ID
    def put(self, id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            data = request.get_json()
            libro.update(data)
            return "", 201
        return "", 404

# Colección de libros
class Libros(Resource):
    # Obtener lista de libros
    def get(self):
        return LIBROS

    # Insertar un nuevo libro
    def post(self):
        libro = request.get_json()
        id = int(max(LIBROS.keys())) + 1
        LIBROS[id] = libro
        return LIBROS[id], 201