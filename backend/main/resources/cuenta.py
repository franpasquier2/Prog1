from flask_restful import Resource, reqparse #reqparse: analizar y validar los datos que llegan en una solicitud HTTP
from flask import request


CUENTAS = {
    1: {"nombre": "Usuario1", "rol": "USER", "password": "123456"},
    2: {"nombre": "Usuario2", "rol": "ADMIN", "password": "abcdef"}
}

USUARIOS = {
    1: {"nombre": "Usuario1", "password": "contraseña123", "rol": "ADMIN"},
    2: {"nombre": "Usuario2", "password": "secreto456", "rol": "BIBLIOTECARIO"}
}

class SignIn(Resource):

    def get(self):
        return CUENTAS
    # Obtener un usuario por nombre
    def post (self):
        cuenta = request.get_json()
        id = int(max(CUENTAS.keys())) + 1
        CUENTAS[id] = cuenta
        return "Se creo la cuenta"

class Login(Resource):
    def get(self):
        return USUARIOS
    # Obtener un usuario por nombre
    def post (self):
        cuenta = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = cuenta
        return "Se inicio la cuenta"