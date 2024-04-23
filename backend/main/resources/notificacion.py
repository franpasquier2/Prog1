from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models import NotificacionModel
#NOTIFICACIONES = {
#    1: {'mensaje': 'Recordatorio de evento', 'tipo': 'Recordatorio'},
#    2: {'mensaje': 'Alerta de seguridad', 'tipo': 'Alerta'}
#}

# Defino el recurso Notificacion


# Colección de notificaciones
class Notificaciones(Resource):
    # Obtener lista de notificaciones
    def get(self):
        notificaciones = db.session.query(NotificacionModel).all()
        return jsonify([notificacion.to_json() for notificacion in notificaciones])
        #return NOTIFICACIONES

    # Insertar una nueva notificación
    def post(self):
        notificaciones = NotificacionModel.from_json(request.get_json())
        db.session.add(notificaciones)
        db.session.commit()
        return notificaciones.to_json(), 201
        
        #notificacion = request.get_json()
        #id = int(max(NOTIFICACIONES.keys())) + 1
        #NOTIFICACIONES[id] = notificacion
        #return NOTIFICACIONES[id], 201