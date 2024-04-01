from flask_restful import Resource, reqparse
from flask import request


CONFIGURACION_BIBLIOTECA = {'nombre': 'Biblioteca XYZ', 'ubicacion': 'Ciudad ABC', 'rol': 'ADMIN'}

LIBROS_DATA = {
    1: {'titulo': 'Libro 1', 'autor': 'Autor 1', 'valoracion': None, 'comentario': None},
    2: {'titulo': 'Libro 2', 'autor': 'Autor 2', 'valoracion': 4.5, 'comentario': 'Buen libro'}
}



class Configuracion(Resource):
    # Obtener configuración general de la biblioteca
    def get(self):
        rol = request.args.get('rol')
        if rol == 'ADMIN':
            return CONFIGURACION_BIBLIOTECA
        return 'Unauthorized', 401

    # Editar configuración de biblioteca
    def put(self):
        if request.args.get('rol') == 'ADMIN':
            parser = reqparse.RequestParser()
            parser.add_argument('nombre', type=str, help='Nombre de la biblioteca')
            parser.add_argument('ubicacion', type=str, help='Ubicación de la biblioteca')
            args = parser.parse_args()
            CONFIGURACION_BIBLIOTECA['nombre'] = args['nombre']
            CONFIGURACION_BIBLIOTECA['ubicacion'] = args['ubicacion']
            return '', 201
        return 'Unauthorized', 401

# Recurso para agregar y obtener valoraciones de libros
class Valoracion(Resource):
    # Agregar una valoración a un libro
    def post(self):
        if request.args.get('rol') == 'USER':
            parser = reqparse.RequestParser()
            parser.add_argument('id_libro', type=int, help='ID del libro a valorar', required=True)
            parser.add_argument('valoracion', type=float, help='Valoración del libro', required=True)
            args = parser.parse_args()
            if args['id_libro'] in LIBROS_DATA:
                LIBROS_DATA[args['id_libro']]['valoracion'] = args['valoracion']
                return LIBROS_DATA[args['id_libro']], 201
            return 'Libro no encontrado', 404
        return 'Unauthorized', 401

    # Obtener valoración de un libro
    def get(self, id_libro):
        rol = request.args.get('rol')
        if rol == 'ADMIN':
            if int(id_libro) in LIBROS_DATA:
                return {'valoracion': LIBROS_DATA[int(id_libro)]['valoracion']}
            return 'Libro no encontrado', 404
        return 'Unauthorized', 401

# Recurso para agregar y obtener comentarios de libros
class Comentarios(Resource):
    # Agregar un comentario a un libro
    def post(self):
        if request.args.get('rol') == 'USER':
            parser = reqparse.RequestParser()
            parser.add_argument('id_libro', type=int, help='ID del libro a comentar', required=True)
            parser.add_argument('comentario', type=str, help='Comentario del libro', required=True)
            args = parser.parse_args()
            if args['id_libro'] in LIBROS_DATA:
                LIBROS_DATA[args['id_libro']]['comentario'] = args['comentario']
                return LIBROS_DATA[args['id_libro']], 201
            return 'Libro no encontrado', 404
        return 'Unauthorized', 401

    # Obtener comentario de un libro
    def get(self, id_libro):
        rol = request.args.get('rol')
        if rol == 'ADMIN':
            if int(id_libro) in LIBROS_DATA:
                return {'comentario': LIBROS_DATA[int(id_libro)]['comentario']}
            return 'Libro no encontrado', 404
        return 'Unauthorized', 401