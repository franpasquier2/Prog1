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
        return usuario.to_json(), 201

    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario.to_json(), 204

    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json() , 201

class Usuarios(Resource):

    def get(self):

        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json_complete() for usuario in usuarios])
    
    def post(self):
        usuarios = UsuarioModel.from_json(request.get_json())
        db.session.add(usuarios)
        db.session.commit()
        return usuarios.to_json(), 201