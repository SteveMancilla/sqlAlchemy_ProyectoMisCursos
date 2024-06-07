from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from MisCursos.src.modelo.declarative_base import Engine, Session, Base


# Relación de muchos a muchos: Tabla de asociación entre alumno y asignaturas
alumno_asignaturas_asociacion = Table('alumno_asignaturas', Base.metadata, 
    Column('alumno_fk', String, ForeignKey('alumno.dni'), primary_key=True),
    Column('asignatura_fk', String, ForeignKey('asignaturas.id'), primary_key=True),
    Column('NombreAsignatura', String))

class Alumno(Base):
    __tablename__ = 'alumno'
    dni = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=True)
    #nacimiento = Column(Date, nullable=True)
    
    asignaturas = relationship('Asignaturas', secondary=alumno_asignaturas_asociacion, back_populates='alumno')


class Asignaturas(Base):
    __tablename__ = 'asignaturas'
    id = Column(String, primary_key=True)
    nombre_asignatura = Column(String, nullable=False)
    valor_creditos = Column(Integer, nullable=False)
    horas_practicas = Column(Integer, nullable=False)
    horas_teoricas = Column(Integer, nullable=False)
    nrc = Column(String, nullable=False)
    
    alumno = relationship('Alumno', secondary=alumno_asignaturas_asociacion, back_populates='asignaturas')