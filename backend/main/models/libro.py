from .. import db
class Libro(db.Model):
    id_libro = db.Column(db.Integer, primary_key=True)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    clasificacion = db.Column(db.Integer, nullable=False)

    def to_json(self):
        libro_json = {
            'id_libro': self.id_libro,
            'id_autor': self.id_autor,
            'titulo': str(self.titulo),
            'genero': str(self.genero),
            'clasificacion': self.clasificacion,
        }
        return libro_json
    
    @staticmethod
    #Convertir JSON a objeto
    def from_json(Libro_json):
        id_libro = Libro_json.get('id_libro')
        id_autor = Libro_json.get('id_autor')
        titulo = Libro_json.get('titulo')
        genero = Libro_json.get('genero')
        clasificacion = Libro_json.get('clasificacion')
        return Libro(id_libro=id_libro,
                    id_autor=id_autor,
                    titulo=titulo,
                    genero=genero,
                    clasificacion=clasificacion,
                    )