from .. import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def to_json(self):
        user_json = {
            'id_usuario': self.id_usuario,
            'username': str(self.username),
            'password': self.password,
            'email': str(self.email),
            'name': str(self.name),            
            # No incluimos la contraseña por seguridad
        }
        return user_json
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