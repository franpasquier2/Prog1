from flask_restful import Resource
from flask import Flask, jsonify, request
from .. import db
from main.models.libro import Libro as LibroModel
from datetime import datetime
from sqlalchemy import func,desc
from main.models import LibroModel, AutorModel, ValoracionModel
# Defino el recurso Libro
class Libro(Resource):
    # Obtener un libro por ID
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json(), 201
        
    # Eliminar un libro por ID
    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return libro.to_json(), 204
    

    # Modificar un libro por ID
    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json() , 201


class Libros(Resource):

    def get(self):

        page = 1
        per_page = 10
        
        libros = db.session.query(LibroModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###
        if request.args.get('nrAutores'):
            libros=libros.outerjoin(LibroModel.autor).group_by(LibroModel.id).having(func.count(AutorModel.id) >= int(request.args.get('nrAutores')))
        
        #Busqueda por titulo
        if request.args.get('titulo'):
            libros=libros.filter(LibroModel.titulo.like("%"+request.args.get('titulo')+"%"))
        
        #Ordeno por titulo
        if request.args.get('sortby_titulo'):
            libros=libros.order_by(desc(LibroModel.titulo))
            
          #Busqueda por genero
        if request.args.get('genero'): 
            libros=libros.filter(LibroModel.genero.like("%"+request.args.get('genero')+"%"))
        
        #Ordeno por genero
        if request.args.get('sortby_genero'):
            libros=libros.order_by(desc(LibroModel.genero))

          #Busqueda por clasificacion
        if request.args.get('clasificacion'): 
            libros=libros.filter(LibroModel.clasificacion.like("%"+request.args.get('clasificacion')+"%"))
        
        #Ordeno por clasificacion
        if request.args.get('sortby_clasificacion'):
            libros=libros.order_by(desc(LibroModel.clasificacion))

        #Ordenao por Autores
        if request.args.get('sortby_nrAutores'):
            animales=animales.outerjoin(LibroModel.autor).group_by(LibroModel.id).order_by(func.count(AutorModel.id).desc())
        ### FIN FILTROS ####
        
        libros = libros.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'libros': [libro.to_json() for libro in libros],
                  'total': libros.total,
                  'paginas': libros.pages,
                  'pagina': page
                })

    def post(self):
        valoraciones_id = request.get_json().get('valoraciones')
        libro = LibroModel.from_json(request.get_json())
        
        if valoraciones_id:
         
            valoraciones = ValoracionModel.query.filter(ValoracionModel.id.in_(valoraciones_id)).all()
        
            libro.valoraciones.extend(valoraciones)
            
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201
  