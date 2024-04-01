from flask_restful import Resource, reqparse
from flask import request

LIBROS = {
    1: {'titulo': 'Libro 1', 'autor': 'Autor 1', 'rol': 'ADMIN'},
    2: {'titulo': 'Libro 2', 'autor': 'Autor 2', 'rol': 'BIBLIOTECARIO'},
    3: {'titulo': 'Libro 3', 'autor': 'Autor 3', 'rol': 'USER'}
}

class Libros(Resource):
    # Obtener lista de libros
    def get(self):
        rol = request.args.get('rol')
        if rol in ['ADMIN', 'BIBLIOTECARIO']:
            return LIBROS
        return 'Unauthorized', 401

    # Crear un libro
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('titulo', type=str, help='Título del libro', required=True)
        parser.add_argument('autor', type=str, help='Autor del libro', required=True)
        args = parser.parse_args()
        if request.args.get('rol') == 'ADMIN':
            id = int(max(LIBROS.keys())) + 1
            LIBROS[id] = {'titulo': args['titulo'], 'autor': args['autor'], 'rol': 'ADMIN'}
            return LIBROS[id], 201
        return 'Unauthorized', 401

# Recurso para obtener, editar y eliminar un libro específico
class Libro(Resource):
    # Obtener un libro
    def get(self, id):
        if int(id) in LIBROS and request.args.get('rol') == 'USER':
            return LIBROS[int(id)]
        return 'Unauthorized', 401

    # Editar un libro
    def put(self, id):
        if int(id) in LIBROS and request.args.get('rol') == 'ADMIN':
            parser = reqparse.RequestParser()
            parser.add_argument('titulo', type=str, help='Título del libro')
            parser.add_argument('autor', type=str, help='Autor del libro')
            args = parser.parse_args()
            libro = LIBROS[int(id)]
            if 'titulo' in args:
                libro['titulo'] = args['titulo']
            if 'autor' in args:
                libro['autor'] = args['autor']
            return '', 201

        return 'Unauthorized', 401

    # Eliminar un libro por ID
    def delete(self, id):
        if int(id) in LIBROS and request.args.get('rol') == 'ADMIN':
            del LIBROS[int(id)]
            return '', 204

        return 'Unauthorized', 401