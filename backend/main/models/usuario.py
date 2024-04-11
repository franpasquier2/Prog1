from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def to_json(self):
        user_json = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            # No incluimos la contraseña por seguridad
        }
        return user_json