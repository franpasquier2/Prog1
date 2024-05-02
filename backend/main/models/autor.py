from .. import db
from datetime import datetime
#Tabla intermedia entre autor y libro

libros_autores = db.Table("libros_autores",
    db.Column("id_libro",db.Integer,db.ForeignKey("libro.id_libro"),primary_key=True),
    db.Column("id_autor",db.Integer,db.ForeignKey("autor.id_autor"),primary_key=True)
    )

class Autor(db.Model):
    id_autor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
      
# Relación uno a muchos entre autores y libros
    libro = db.relationship("Libro" ,back_populates = "autor", secondary = "libros_autores")
    
    def _repr_(self):                    
        return '<Autor: %r >' % (self.nombre)


    def to_json(self):
        autor_json = {
            'id_autor': self.id_autor,
            'nombre': str(self.nombre),
            'fecha': str(self.fecha.strftime("%d-%m-%Y")),
        }
        return autor_json
    
    def to_json_short(self):
        autor_json={
            'id_autor':self.id_autor,
            'nombre':str(self.nombre),
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
    
