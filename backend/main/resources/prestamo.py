from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.prestamo import Prestamo as PrestamoModel
from datetime import datetime
from sqlalchemy import func,desc
from main.models import PrestamoModel, UsuarioModel
class Prestamo(Resource):

    def get(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        return prestamo.to_json(), 201
       
    def delete(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return prestamo.to_json(), 204

    def put(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            if key == "fecha_dev":
                fecha_dev = datetime.strptime(value, '%d-%m-%Y')
                setattr(prestamo, key, fecha_dev)
            elif key == "fecha":
                fecha = datetime.strptime(value, '%d-%m-%Y')
                setattr(prestamo, key, fecha)
            else:
                setattr(prestamo, key, value)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json() , 201


class Prestamos(Resource):
    
    def get(self):
       
        page = 1
        per_page = 10

        prestamos = db.session.query(PrestamoModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###
        if request.args.get('nrUsuarios'):
            prestamos=prestamos.outerjoin(PrestamoModel.usuario).group_by(PrestamoModel.id).having(func.count(UsuarioModel.id) >= int(request.args.get('nrUsuarios')))
        
        #Busqueda por monto
        if request.args.get('monto'):
            prestamos=prestamos.filter(PrestamoModel.monto.like("%"+request.args.get('monto')+"%"))
        
        #Ordeno por monto
        if request.args.get('sortby_monto'):
            prestamos=prestamos.order_by(desc(PrestamoModel.monto))
            
          #Busqueda por fecha_dev
        if request.args.get('fecha_dev'): 
            prestamos=prestamos.filter(PrestamoModel.fecha_dev.like("%"+request.args.get('fecha_dev')+"%"))
        
        #Ordeno por fecha_dev
        if request.args.get('sortby_fecha_dev'):
            prestamos=prestamos.order_by(desc(PrestamoModel.fecha_dev))

          #Busqueda por fecha
        if request.args.get('fecha'): 
            prestamos=prestamos.filter(PrestamoModel.fecha.like("%"+request.args.get('fecha')+"%"))
        
        #Ordeno por fecha
        if request.args.get('sortby_fecha'):
            prestamos=prestamos.order_by(desc(PrestamoModel.fecha))

        #Ordenao por Usuarios
        if request.args.get('sortby_nrUsuarios'):
            animales=animales.outerjoin(PrestamoModel.usuario).group_by(PrestamoModel.id).order_by(func.count(UsuarioModel.id).desc())
        ### FIN FILTROS ####
        
        prestamos = prestamos.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'prestamos': [prestamo.to_json() for prestamo in prestamos],
                  'total': prestamos.total,
                  'paginas': prestamos.pages,
                  'pagina': page
                })

    def post(self):
        usuarios_id = request.get_json().get('usuarios')
        prestamo = PrestamoModel.from_json(request.get_json())
        
        if usuarios_id:
         
            usuarios = UsuarioModel.query.filter(UsuarioModel.id.in_(usuarios_id)).all()
        
            prestamo.usuarios.extend(usuarios)
            
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201