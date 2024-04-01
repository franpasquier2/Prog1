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
 
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<:id>')
    api.add_resource(resources.Libros, '/libros')
    api.add_resource(resources.Libro, '/libro/<:id>')
    api.add_resource(resources.SignIn, '/signin')
    api.add_resource(resources.Login, '/login')
    api.add_resource(resources.Notificaciones, '/notificaciones')
    api.add_resource(resources.Configuracion, '/configuracion')
    api.add_resource(resources.Comentarios, '/comentarios')
    api.add_resource(resources.Valoracion, '/valoracion')
    
    #Cargar la aplicacion en la API de Flask Restful
    #es para que la aplicacion de flask funcione como API
    api.init_app(app)
    #Por ultimo retornamos la aplicacion iniializada
    return app