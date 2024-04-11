from flask_restful import Resource
from flask import request

PRESTAMOS = {
    1: {'id_usuario': 1, 'libro': 'Harry Potter', 'fecha_prestamo': '2024-04-01', 'fecha_devolucion': '2024-04-15'},
    2: {'id_usuario': 2, 'libro': 'El Señor de los Anillos', 'fecha_prestamo': '2024-03-25', 'fecha_devolucion': '2024-04-10'}
}

# Defino el recurso Préstamo
class Prestamo(Resource):
    # Obtener un préstamo por ID
    def get(self, id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)]
        return '', 404

    # Eliminar un préstamo por ID
    def delete(self, id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS[int(id)]
            return '', 204
        return '', 404

    # Modificar un préstamo por ID
    def put(self, id):
        if int(id) in PRESTAMOS:
            prestamo = PRESTAMOS[int(id)]
            data = request.get_json()
            prestamo.update(data)
            return '', 201
        return '', 404

# Colección de préstamos
class Prestamos(Resource):
    # Obtener lista de préstamos
    def get(self):
        return PRESTAMOS

    # Insertar un nuevo préstamo
    def post(self):
        prestamo = request.get_json()
        id = int(max(PRESTAMOS.keys())) + 1
        PRESTAMOS[id] = prestamo
        return PRESTAMOS[id], 201