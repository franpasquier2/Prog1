from .. import db
class Libro(db.Model):
    id_libro = db.Column(db.Integer, primary_key=True)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    clasificacion = db.Column(db.Integer, nullable=False)
#Relacion muchos a muchos con libros_autores
    autor = db.relationship('Autor' ,back_populates = 'libro' ,secondary = 'libros_autores')
# Relación un libro a una valoracion
    valoracion = db.relationship('Valoracion', back_populates='libro', cascade="all, delete-orphan",uselist=False, single_parent=True)
# Relación un usuario a muchos libros
    usuario = db.relationship('Usuario', back_populates='libros', uselist=False, single_parent=True)
    

    def __repr__(self):                    
        return '<Libro: %r >' % (self.titulo)
    
    def to_json(self):
        libro_json = {
            'id_libro': self.id_libro,
            'id_autor':self.id_autor,
            'id_usuario':self.id_usuario,
            'titulo': str(self.titulo),
            'genero': str(self.genero),
            'clasificacion': self.clasificacion,
        }
        return libro_json
    
    def to_json_short(self):
        libro_json={
            'id_libro':self.id_libro,
            'titulo':str(self.titulo),
            'genero':str(self.genero)
        }
        return libro_json

    def to_json_complete(self):
        autor = [autor.to_json() for autor in self.autor]
        autor_json={
            'id_libro': self.id_libro,
            'id_autor':self.id_autor,
            'id_usuario':self.id_usuario,
            'titulo': str(self.titulo),
            'genero': str(self.genero),
            'clasificacion': self.clasificacion,
            'autor': autor
        }
        return autor_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(Libro_json):
        id_libro = Libro_json.get('id_libro')
        id_autor = Libro_json.get('id_autor')
        id_usuario = Libro_json.get('id_usuario')
        titulo = Libro_json.get('titulo')
        genero = Libro_json.get('genero')
        clasificacion = Libro_json.get('clasificacion')
        return Libro(id_libro=id_libro,
                    id_autor=id_autor,
                    id_usuario=id_usuario,
                    titulo=titulo,
                    genero=genero,
                    clasificacion=clasificacion,
                    )