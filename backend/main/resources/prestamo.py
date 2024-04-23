from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.prestamo import Prestamo as PrestamoModel
from datetime import datetime

#PRESTAMOS = {
#    1: {'id_Prestamo': 1, 'libro': 'Harry Potter', 'fecha_prestamo': '2024-04-01', 'fecha_devolucion': '2024-04-15'},
#    2: {'id_Prestamo': 2, 'libro': 'El Señor de los Anillos', 'fecha_prestamo': '2024-03-25', 'fecha_devolucion': '2024-04-10'}
#}

# Defino el recurso Préstamo
class Prestamo(Resource):
    # Obtener un préstamo por ID
    def get(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        return prestamo.to_json(), 201
        #if int(id) in PRESTAMOS:
        #    return PRESTAMOS[int(id)]
        #return '', 404

    # Eliminar un préstamo por ID
    def delete(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return prestamo.to_json(), 204
        #if int(id) in PRESTAMOS:
        #    del PRESTAMOS[int(id)]
        #    return '', 204
        #return '', 404

    # Modificar un préstamo por ID
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


        #if int(id) in PRESTAMOS:
        #    prestamo = PRESTAMOS[int(id)]
        #    data = request.get_json()
        #    prestamo.update(data)
        #    return '', 201
        #return '', 404

# Colección de préstamos
class Prestamos(Resource):
    # Obtener lista de préstamos
    def get(self):
        prestamos = db.session.query(PrestamoModel).all()
        return jsonify([prestamos.to_json() for prestamos in prestamos])

        #return PRESTAMOS

    # Insertar un nuevo préstamo
    def post(self):
        prestamos = PrestamoModel.from_json(request.get_json())
        db.session.add(prestamos)
        db.session.commit()
        return prestamos.to_json(), 201

        #prestamo = request.get_json()
        #id = int(max(PRESTAMOS.keys())) + 1
        #PRESTAMOS[id] = prestamo
        #return PRESTAMOS[id], 201