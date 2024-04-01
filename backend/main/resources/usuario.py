from flask_restful import Resource, reqparse
from flask import request

# Datos de prueba en JSON
USUARIOS = {
    1: {'nombre': 'Juan', 'rol': 'ADMIN'},
    2: {'nombre': 'María', 'rol': 'BIBLIOTECARIO'}
}

class Usuarios(Resource):
    # Obtener listado de usuarios
    def get(self):
        if request.args.get('rol') == 'ADMIN':
            return USUARIOS
        return 'Unauthorized', 401

    # Crear un usuario
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, help='Nombre del usuario', required=True)
        parser.add_argument('rol', type=str, help='Rol del usuario', required=True)
        args = parser.parse_args()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = {'nombre': args['nombre'], 'rol': args['rol']}
        return USUARIOS[id], 201

# Defino el recurso Usuario
class Usuario(Resource):
    # Obtener un usuario
    def get(self, id):
        if int(id) in USUARIOS and request.args.get('rol') == 'ADMIN':
            return USUARIOS[int(id)]
        return 'Unauthorized', 401

    # Editar un usuario
    def put(self, id):
        if int(id) in USUARIOS and request.args.get('rol') == 'ADMIN':
            parser = reqparse.RequestParser()
            parser.add_argument('nombre', type=str, help='Nombre del usuario')
            parser.add_argument('rol', type=str, help='Rol del usuario')
            args = parser.parse_args()
            user = USUARIOS[int(id)]
            if 'nombre' in args:
                user['nombre'] = args['nombre']
            if 'rol' in args:
                user['rol'] = args['rol']
            return '', 201

        return 'Unauthorized', 401

    