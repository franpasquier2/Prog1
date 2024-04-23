from .. import db
from datetime import datetime
class Autor(db.Model):
    id_autor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        autor_json = {
            'id_autor': self.id_autor,
            'nombre': str(self.nombre),
            'fecha': str(self.fecha.strftime("%d-%m-%Y")),
        }
        return autor_json
    
    @staticmethod
    #Convertir JSON a objeto
    def from_json(Autor_json):
        id_autor = Autor_json.get('id_autor')
        nombre = Autor_json.get('nombre')
        fecha = datetime.strptime(Autor_json.get('fecha'), "%d-%m-%Y")
        return Autor(id_autor=id_autor,
                    nombre=nombre,
                    fecha=fecha,
                    )