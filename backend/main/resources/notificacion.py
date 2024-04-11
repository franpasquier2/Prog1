from flask_restful import Resource
from flask import request

NOTIFICACIONES = {
    1: {'mensaje': 'Recordatorio de evento', 'tipo': 'Recordatorio'},
    2: {'mensaje': 'Alerta de seguridad', 'tipo': 'Alerta'}
}

# Defino el recurso Notificacion


# Colección de notificaciones
class Notificaciones(Resource):
    # Obtener lista de notificaciones
    def get(self):
        return NOTIFICACIONES

    # Insertar una nueva notificación
    def post(self):
        notificacion = request.get_json()
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[id] = notificacion
        return NOTIFICACIONES[id], 201