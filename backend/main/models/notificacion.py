from .. import db
from datetime import datetime
class Notificacion(db.Model):
    id_notificacion = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id_usuario'), nullable=False)
    fecha_dev = db.Column(db.DateTime, nullable=False)
    mensaje = db.Column(db.String(100), nullable=False)
    
#Relación un usuario a muchos libros
    usuario = db.relationship('Usuario', back_populates='notificaciones', single_parent=True)
    
    def _repr_(self):                    
        return '<Notificacion: %r >' % (self.mensaje)

    def to_json(self):
        notificacion_json = {
            'id_notificacion': self.id_notificacion,
            'id_usuario': self.id_usuario,
            'fecha_dev':str(self.fecha_dev.strftime("%d-%m-%Y")),  
            'mensaje': self.mensaje,
        }
        return notificacion_json
    
    def to_json_short(self):
        notificacion_json={
            'id_notificacion':self.id_notificacion,
            'mensaje':str(self.mensaje)
        }
        return notificacion_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(Notificacion_json):
        id_notificacion = Notificacion_json.get('id_notificacion')
        id_usuario = Notificacion_json.get('id_usuario')
        fecha_dev = datetime.strptime(Notificacion_json.get('fecha_dev'), "%d-%m-%Y")
        mensaje = Notificacion_json.get('mensaje')
        return Notificacion(id_notificacion=id_notificacion,
                    id_usuario=id_usuario,
                    fecha_dev=fecha_dev,
                    mensaje=mensaje,
                    )