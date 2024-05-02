from .. import db

class Valoracion(db.Model):
    id_valoracion = db.Column(db.Integer, primary_key=True)
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id_libro'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    puntuacion = db.Column(db.Integer, nullable=False)
    
# Relación un libro a una valoracion
    libro = db.relationship('Libro', back_populates='valoracion', cascade="all, delete-orphan",uselist=False, single_parent=True)
    
    def __repr__(self):                    
        return '<Valoracion: %r >' % (self.puntuacion)
    
    def to_json(self):
        valoracion_json = {
            'id_valoracion': self.id_valoracion,
            'id_libro': self.id_libro,
            'id_usuario': self.id_usuario,
            'puntuacion': self.puntuacion,
        }
        return valoracion_json
    
    def to_json_short(self):
        valoracion_json={
            'id_valoracion':self.id_valoracion,
            'puntuacion':self.puntuacion
        }
        return valoracion_json

    @staticmethod
    #Convertir JSON a objetoimport datetime
    def from_json(Valoracion_json):
        id_valoracion = Valoracion_json.get('id_valoracion')
        id_libro = Valoracion_json.get('id_libro')
        id_usuario = Valoracion_json.get('id_usuario')
        puntuacion = Valoracion_json.get('puntuacion')
        return Valoracion(id_valoracion=id_valoracion,
                    id_libro=id_libro,
                    id_usuario=id_usuario,
                    puntuacion=puntuacion
                    )