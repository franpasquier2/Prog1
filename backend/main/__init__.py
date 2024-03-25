<<<<<<< HEAD
# La carpeta main va a tener todo el codigo menos app.py
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

# Inicializar la API de flask RestFul
api = Api()

#Vamos a crear un metodo que inicializara la app y todos los modulos
def create_app():
    #Inicio flask
    app = Flask(__name__)

    #cargamos las variables del archivo .env
    load_dotenv()
 
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
    
    #Cargar la aplicacion en la API de Flask Restful
    #es para que la aplicacion de flask funcione como API
    api.init_app(app)
    #Por ultimo retornamos la aplicacion iniializada
    return app
=======
    
>>>>>>> Nueva Rama toneatti
