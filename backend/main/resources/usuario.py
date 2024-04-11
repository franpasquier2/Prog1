from flask import Flask, request
from flask_restful import Resource
from .. import db
from main.models.usuario import Usuario as UserModel

USUARIOS = {
    1: {'nombre': 'Juan', 'rol': 'ADMIN'},
    2: {'nombre': 'María', 'rol': 'BIBLIOTECARIO'}
}

# Defino el recurso Usuario
class Usuario(Resource):

    def get(self, id):

        usuario = db.session.query(UserModel).get_or_404(id)
        return usuario.to_json()
    #    if int(id) in USUARIOS:
    #       return USUARIOS[int(id)]
    #    return '', 404

    # Eliminar un usuario por ID
    def delete(self, id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return '', 204
        return '', 404

    # Modificar un usuario por ID
    def put(self, id):
        if int(id) in USUARIOS:
            user = USUARIOS[int(id)]
            data = request.get_json()
            user.update(data)
            return '', 201
        return '', 404

# Colección de usuarios
class Usuarios(Resource):
    # Obtener lista de usuarios
    def get(self):
        return USUARIOS

    # Insertar un nuevo usuario
    def post(self):
        user = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = user
        return USUARIOS[id], 201

    