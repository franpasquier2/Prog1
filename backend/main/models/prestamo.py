from .. import db
from datetime import datetime

class Prestamo(db.Model):
    id_prestamo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id_usuario'), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha_dev = db.Column(db.DateTime, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    
#Relación un usuario a muchos prestamos
    usuario = db.relationship('Usuario', back_populates='prestamos', uselist=False, single_parent=True)
    
    def _repr_(self):                    
        return '<Prestamo: %r >' % (self.monto)

    def to_json(self):
        prestamo_json = {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'monto': self.monto,
            'fecha_dev':str(self.fecha_dev.strftime("%d-%m-%Y")),  
            'fecha':str(self.fecha.strftime("%d-%m-%Y")),  
        }
        return prestamo_json
    
    def to_json_short(self):
        prestamo_json={
            'id_prestamo':self.id_prestamo,
            'id_usuario':self.id_usuario,
            'monto':self.monto
        }
        return prestamo_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(Prestamo_json):
        id_prestamo = Prestamo_json.get('id_prestamo')
        id_usuario = Prestamo_json.get('id_usuario')
        monto = Prestamo_json.get('monto')
        fecha_dev = datetime.strptime(Prestamo_json.get('fecha_dev'), "%d-%m-%Y")
        fecha = datetime.strptime(Prestamo_json.get('fecha'), "%d-%m-%Y")
        return Prestamo(id_prestamo=id_prestamo,
                    id_usuario=id_usuario,
                    monto=monto,
                    fecha_dev=fecha_dev,
                    fecha=fecha,
                    )