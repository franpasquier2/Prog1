from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    #Mail usado como nombre de usuario
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    #Contraseña que será el hash de la pass en texto plano
    password = db.Column(db.String(128), nullable=False)
    #Rol (En el caso que existan diferentes tipos de usuarios/Usuarioes con diferentes permisos)
    rol = db.Column(db.String(10), nullable=False, server_default="users")
    
#Relacion un usuario a muchos libros
    libros = db.relationship("Libro" ,back_populates = "usuario", cascade="all, delete-orphan")
#Relacion un usuario a muchos prestamos
    prestamos = db.relationship("Prestamo" ,back_populates = "usuario", cascade="all, delete-orphan")
#Relacion un usuario a muchas notificaciones
    notificaciones = db.relationship("Notificacion" ,back_populates = "usuario", cascade="all, delete-orphan")

#Un 'hash' es el resultado de aplicar una función matemática que toma una entrada y la transforma en una cadena de caracteres, generalmente una representación alfanumérica de longitud fija de los datos de entrada.
    @property
    def plain_password(self): # plain_password evita que se pueda acceder a la contrasena en texto plano 
        raise AttributeError('Password cant be read')
    #Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        return check_password_hash(self.password, password)
    
    def _repr_(self):                    
        return '<Usuario: %r >' % (self.name)

    def to_json(self):
        usuario_json = {
            'id_usuario': self.id_usuario,
            'username': str(self.username),
            'password': self.password,
            'email': str(self.email),
            'name': str(self.name),
            'rol': str(self.rol),           
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
        password = Usuario_json.get('password')
        rol = Usuario_json.get('rol')
        return Usuario(id_usuario=id_usuario,
                    username=username,
                    password=password,
                    email=email,
                    name=name,
                    plain_password=password,
                    rol=rol,
                    )