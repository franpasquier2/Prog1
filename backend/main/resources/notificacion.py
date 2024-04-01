from flask_restful import Resource, reqparse
from flask import request

NOTIFICACIONES = []

class Notificaciones(Resource):
    # Enviar notificación a un usuario
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('usuario', type=str, help='Usuario a notificar', required=True)
        parser.add_argument('mensaje', type=str, help='Mensaje de la notificación', required=True)
        args = parser.parse_args()
        if request.args.get('rol') == 'ADMIN':
            notificacion = {'usuario': args['usuario'], 'mensaje': args['mensaje']}
            NOTIFICACIONES.append(notificacion)
            return notificacion, 201
        return 'Unauthorized', 401