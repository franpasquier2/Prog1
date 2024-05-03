from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models import NotificacionModel
from sqlalchemy import func,desc
from main.models import UsuarioModel
class Notificaciones(Resource):
    
    def get(self):

        page = 1
        per_page = 10
        
        notificaciones = db.session.query(NotificacionModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###
        if request.args.get('nrUsuarios'):
            notificaciones=notificaciones.outerjoin(NotificacionModel.usuario).group_by(NotificacionModel.id).having(func.count(UsuarioModel.id) >= int(request.args.get('nrUsuarios')))
        
        #Busqueda por mensaje
        if request.args.get('mensaje'):
            notificaciones=notificaciones.filter(NotificacionModel.mensaje.like("%"+request.args.get('mensaje')+"%"))
        
        #Ordeno por mensaje
        if request.args.get('sortby_mensaje'):
            notificaciones=notificaciones.order_by(desc(NotificacionModel.mensaje))
            
          #Busqueda por fecha_dev
        if request.args.get('fecha_dev'): 
            notificaciones=notificaciones.filter(NotificacionModel.fecha_dev.like("%"+request.args.get('fecha_dev')+"%"))
        
        #Ordeno por fecha_dev
        if request.args.get('sortby_fecha_dev'):
            notificaciones=notificaciones.order_by(desc(NotificacionModel.fecha_dev))

        #Ordenao por Usuarios
        if request.args.get('sortby_nrUsuarios'):
            animales=animales.outerjoin(NotificacionModel.usuario).group_by(NotificacionModel.id).order_by(func.count(UsuarioModel.id).desc())
        ### FIN FILTROS ####
        
        
        #Obtener valor paginado
        notificaciones = notificaciones.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'notificaciones': [notificacion.to_json() for notificacion in notificaciones],
                  'total': notificaciones.total,
                  'paginas': notificaciones.pages,
                  'pagina': page
                })

    def post(self):
        usuarios_id = request.get_json().get('usuarios')
        notificacion = NotificacionModel.from_json(request.get_json())
        
        if usuarios_id:
         
            usuarios = UsuarioModel.query.filter(UsuarioModel.id.in_(usuarios_id)).all()
        
            notificacion.usuarios.extend(usuarios)
            
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201