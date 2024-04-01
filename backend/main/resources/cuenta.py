from flask_restful import Resource, reqparse #reqparse: analizar y validar los datos que llegan en una solicitud HTTP
from flask import request


SESION = {
    1: {'nombre': 'Usuario1', 'rol': 'USER', 'password': '123456'},
    2: {'nombre': 'Usuario2', 'rol': 'ADMIN', 'password': 'abcdef'}
}

class SignIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, help='Nombre del usuario', required=True)
        parser.add_argument('password', type=str, help='Contraseña del usuario', required=True)
        args = parser.parse_args()
        id = int(max(SESION.keys())) + 1
        SESION[id] = {'nombre': args['nombre'], 'rol': 'USER', 'password': args['password']}
        return SESION[id], 201


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, help='Nombre del usuario', required=True)
        parser.add_argument('password', type=str, help='Contraseña del usuario', required=True)
        args = parser.parse_args()
        for id, user in SESION.items():
            if user['nombre'] == args['nombre'] and user['password'] == args['password']:
                return {'message': 'Login successful', 'rol': user['rol']}, 200
        return 'Unauthorized', 401