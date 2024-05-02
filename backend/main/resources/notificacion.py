from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models import NotificacionModel

class Notificaciones(Resource):
    
    def get(self):
        notificaciones = db.session.query(NotificacionModel).all()
        return jsonify([notificacion.to_json() for notificacion in notificaciones])

    def post(self):
        notificaciones = NotificacionModel.from_json(request.get_json())
        db.session.add(notificaciones)
        db.session.commit()
        return notificaciones.to_json(), 201