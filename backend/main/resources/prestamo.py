from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.prestamo import Prestamo as PrestamoModel
from datetime import datetime

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
        prestamos = db.session.query(PrestamoModel).all()
        return jsonify([prestamos.to_json() for prestamos in prestamos])

    def post(self):
        prestamos = PrestamoModel.from_json(request.get_json())
        db.session.add(prestamos)
        db.session.commit()
        return prestamos.to_json(), 201