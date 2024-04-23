from flask import Flask, jsonify, request
from flask_restful import Resource
from .. import db
from main.models.usuario import Usuario as UsuarioModel

#USUARIOS = {
#    1: {'nombre': 'Juan', 'rol': 'ADMIN'},
#    2: {'nombre': 'María', 'rol': 'BIBLIOTECARIO'}
#}

# Defino el recurso Usuario
class Usuario(Resource):

    def get(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return usuario.to_json()
    #    if int(id) in USUARIOS:
    #       return USUARIOS[int(id)]
    #    return '', 404

    # Eliminar un usuario por ID
    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario.to_json(), 204
        #if int(id) in USUARIOS:
        #    del USUARIOS[int(id)]
        #    return '', 204
        #return '', 404

    # Modificar un usuario por ID
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json() , 201
        #if int(id) in USUARIOS:
        #    Usuario = USUARIOS[int(id)]
        #    data = request.get_json()
        #    Usuario.update(data)
        #    return '', 201
        #return '', 404

# Colección de usuarios
class Usuarios(Resource):
    # Obtener lista de usuarios
    def get(self):

        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuarios.to_json() for usuarios in usuarios])

        #return USUARIOS

    # Insertar un nuevo usuario
    def post(self):
        usuarios = UsuarioModel.from_json(request.get_json())
        db.session.add(usuarios)
        db.session.commit()
        return usuarios.to_json(), 201

        #Usuario = request.get_json()
        #id = int(max(USUARIOS.keys())) + 1
        #USUARIOS[id] = Usuario
        #return USUARIOS[id], 201

    