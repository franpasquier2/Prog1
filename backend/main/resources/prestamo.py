from flask_restful import Resource, reqparse
from flask import request

PRESTAMOS = {
    1: {'usuario': 'Usuario1', 'libro': 'Libro1', 'estado': 'activo', 'rol': 'ADMIN'},
    2: {'usuario': 'Usuario2', 'libro': 'Libro2', 'estado': 'inactivo', 'rol': 'ADMIN'}
}


class Prestamos(Resource):
    # Obtener todos los préstamos
    def get(self):
        rol = request.args.get('rol')
        if rol == 'ADMIN':
            return PRESTAMOS
        return 'Unauthorized', 401

    # Crear un préstamo
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('usuario', type=str, help='Usuario del préstamo', required=True)
        parser.add_argument('libro', type=str, help='Libro del préstamo', required=True)
        parser.add_argument('estado', type=str, help='Estado del préstamo', required=True)
        args = parser.parse_args()
        if request.args.get('rol') == 'ADMIN':
            id = int(max(PRESTAMOS.keys())) + 1
            PRESTAMOS[id] = {'usuario': args['usuario'], 'libro': args['libro'], 'estado': args['estado'], 'rol': 'ADMIN'}
            return PRESTAMOS[id], 201
        return 'Unauthorized', 401

# Recurso para obtener, modificar y eliminar un préstamo específico
class Prestamo(Resource):
    # Obtener un préstamo
    def get(self, id):
        if int(id) in PRESTAMOS and request.args.get('rol') == 'ADMIN':
            return PRESTAMOS[int(id)]
        return 'Unauthorized', 401

    # Modificar un préstamo
    def put(self, id):
        if int(id) in PRESTAMOS and request.args.get('rol') == 'ADMIN':
            parser = reqparse.RequestParser()
            parser.add_argument('usuario', type=str, help='Usuario del préstamo')
            parser.add_argument('libro', type=str, help='Libro del préstamo')
            parser.add_argument('estado', type=str, help='Estado del préstamo')
            args = parser.parse_args()
            prestamo = PRESTAMOS[int(id)]
            if 'usuario' in args:
                prestamo['usuario'] = args['usuario']
            if 'libro' in args:
                prestamo['libro'] = args['libro']
            if 'estado' in args:
                prestamo['estado'] = args['estado']
            return '', 201

        return 'Unauthorized', 401

    # Eliminar un préstamo por ID
    def delete(self, id):
        if int(id) in PRESTAMOS and request.args.get('rol') == 'ADMIN':
            del PRESTAMOS[int(id)]
            return '', 204

        return 'Unauthorized', 401