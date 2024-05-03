from flask import Flask, jsonify, request
from flask_restful import Resource
from .. import db
from main.models.usuario import Usuario as UsuarioModel
from sqlalchemy import func,desc
from main.models import PrestamoModel, LibroModel

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

        page = 1
        per_page = 10
        
        usuarios = db.session.query(UsuarioModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###
        
        if request.args.get('nrLibros'):
            usuarios=usuarios.outerjoin(UsuarioModel.libro).group_by(UsuarioModel.id).having(func.count(LibroModel.id) >= int(request.args.get('nrLibros')))
        
        #Busqueda por username
        if request.args.get('username'):
            usuarios=usuarios.filter(UsuarioModel.username.like("%"+request.args.get('username')+"%"))
        
        #Ordeno por username
        if request.args.get('sortby_username'):
            usuarios=usuarios.order_by(desc(UsuarioModel.username))
            
          #Busqueda por email
        if request.args.get('email'): 
            usuarios=usuarios.filter(UsuarioModel.email.like("%"+request.args.get('email')+"%"))
        
        #Ordeno por email
        if request.args.get('sortby_email'):
            usuarios=usuarios.order_by(desc(UsuarioModel.email))

        #Busqueda por name
        if request.args.get('name'):
            prestamos=prestamos.filter(PrestamoModel.name.like("%"+request.args.get('name')+"%"))
        
        #Ordeno por name
        if request.args.get('sortby_name'):
            prestamos=prestamos.order_by(desc(PrestamoModel.name))

        #Ordeno por id de libro 
        if request.args.get('sortby_nrLibros'):
            usuarios=usuarios.outerjoin(UsuarioModel.libro).group_by(UsuarioModel.id).order_by(func.count(LibroModel.id).desc())
        
        ### FIN FILTROS ####
        
        usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                  'total': usuarios.total,
                  'pages': usuarios.pages,
                  'page': page
                })

    def post(self):
        prestamos_ids = request.get_json().get('prestamos')
        usuario = UsuarioModel.from_json(request.get_json())
        
        if prestamos_ids:
          
            prestamos = PrestamoModel.query.filter(PrestamoModel.id.in_(prestamos_ids)).all()
           
            usuario.prestamos.extend(prestamos)
            
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201