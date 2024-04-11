from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os


api = Api()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    load_dotenv()



    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))
        
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    import main.resources as resources
 

    api.add_resource(resources.UsuariosResources, '/usuarios')
    api.add_resource(resources.UsuarioResources, '/usuario/<id>')
    api.add_resource(resources.LibrossResources, '/libros')
    api.add_resource(resources.LibroResources, '/libro/<id>')
    api.add_resource(resources.SignInResources, '/signin')
    api.add_resource(resources.LoginResources, '/login')
    api.add_resource(resources.NotificacionesResources, '/notificaciones')
    api.add_resource(resources.ConfiguracionResources, '/configuracion/<id>')
    api.add_resource(resources.ConfiguracionesResources, '/configuraciones')
    api.add_resource(resources.ComentariosResources, '/comentarios')
    api.add_resource(resources.ValoracionResources, '/valoracion')
    api.add_resource(resources.PrestamosResources, '/prestamos')
    api.add_resource(resources.PrestamoResources, '/prestamo/<id>')
    
    api.init_app(app)


    return app