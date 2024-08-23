from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseDeDatos = declarative_base()


class Estudiante(BaseDeDatos):

    __tablename__ = "estudiante"

    id = Column(Integer, primary_key=True, index=True)
    nombre =  Column(String(100))
    apellido = Column(String(100))
    edad = Column(Integer)
    mail = Column(String(100), unique=True)
    matricula = Column(String(20), unique=True)
    carrera = Column(String(100))
    publicaciones = relationship("Publicacion", back_populates="estudiante")

    def __init__(self, nombre, apellido, edad, mail, matricula, carrera, id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
        self.matricula = matricula
        self.carrera = carrera

class Publicacion(BaseDeDatos):

    __tablename__ = "publicaciones"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100))
    contenido = Column(String(500))
    estudiante_id = Column(Integer, ForeignKey('estudiante.id'))
    estudiante = relationship("Estudiante", back_populates="publicaciones")

    def __init__(self, titulo, contenido, estudiante_id, id=None):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.estudiante_id = estudiante_id
