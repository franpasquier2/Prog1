from .. import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
#Relacion un usuario a muchos libros
    libros = db.relationship("Libro" ,back_populates = "usuario", cascade="all, delete-orphan")
#Relacion un usuario a muchos prestamos
    prestamos = db.relationship("Prestamo" ,back_populates = "usuario", cascade="all, delete-orphan")
#Relacion un usuario a muchas notificaciones
    notificaciones = db.relationship("Notificacion" ,back_populates = "usuario", cascade="all, delete-orphan")
    
    def _repr_(self):                    
        return '<Usuario: %r >' % (self.name)

    def to_json(self):
        usuario_json = {
            'id_usuario': self.id_usuario,
            'username': str(self.username),
            'password': self.password,
            'email': str(self.email),
            'name': str(self.name),            
            # No incluimos la contraseña por seguridad
        }
        return usuario_json

    def to_json_short(self):
        usuario_json={
            'id_usuario':self.id_usuario,
            'username':str(self.username),
            'email':str(self.email)
        }
        return usuario_json

    def to_json_complete(self):
        prestamo = [prestamo.to_json() for prestamo in self.prestamos]
        prestamo_json={
            'id_usuario':self.id_usuario,
            'username':str(self.username),
            'email':str(self.email),
            'name':str(self.name),
            'prestamo': prestamo
        }
        return prestamo_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(Usuario_json):
        id_usuario = Usuario_json.get('id_usuario')
        username = Usuario_json.get('username')
        password = Usuario_json.get('password')
        email = Usuario_json.get('email')
        name = Usuario_json.get('name')
        return Usuario(id_usuario=id_usuario,
                    username=username,
                    password=password,
                    email=email,
                    name=name,
                    )