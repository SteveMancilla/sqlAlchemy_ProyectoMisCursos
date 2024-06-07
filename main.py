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


# Si queremos ejecutar una y otra vez pongo lo siguiente, para eliminar cuando se ejecute y con la mima volver a crear la base de datos
Base.metadata.drop_all(Engine)

# Crear todas las tablas
Base.metadata.create_all(Engine)

# Crear una sesión
session = Session()

# Crear instancias de alumnos
new_alumno1 = Alumno(dni='72620878', nombre='Steven', apellido='Huaccho Mancilla', edad=19)
new_alumno2 = Alumno(dni='5945', nombre='Joel', apellido='Lazo Maravi', edad=19)
new_alumno3 = Alumno(dni='08541', nombre='Andrea', apellido='Rojas Mellado', edad=19)

# Crear instancias de asignaturas
new_asignatura1 = Asignaturas(id='CS101', nombre_asignatura='Cons. Software', valor_creditos=4, horas_practicas=4, horas_teoricas=2, nrc='2024_02180')
new_asignatura2 = Asignaturas(id='OS101', nombre_asignatura='Sistemas operativos', valor_creditos=4, horas_practicas=0, horas_teoricas=2, nrc='2023_02180')
new_asignatura3 = Asignaturas(id='DS101', nombre_asignatura='Diseño de software', valor_creditos=4, horas_practicas=4, horas_teoricas=2, nrc='2024_01180')
new_asignatura4 = Asignaturas(id='RC101', nombre_asignatura='Redes de computadoras', valor_creditos=4, horas_practicas=6, horas_teoricas=0, nrc='2024_12180')
new_asignatura5 = Asignaturas(id='POO101', nombre_asignatura='Programacion orientado a objetos', valor_creditos=4, horas_practicas=4, horas_teoricas=2, nrc='15224_02180')

# Asignar asignaturas a alumnos
new_alumno1.asignaturas.append(new_asignatura1)
new_alumno1.asignaturas.append(new_asignatura2)
new_alumno1.asignaturas.append(new_asignatura3)
new_alumno1.asignaturas.append(new_asignatura4)
new_alumno2.asignaturas.append(new_asignatura5)
new_alumno2.asignaturas.append(new_asignatura2)
new_alumno2.asignaturas.append(new_asignatura1)
new_alumno3.asignaturas.append(new_asignatura4)
new_alumno3.asignaturas.append(new_asignatura5)
new_alumno3.asignaturas.append(new_asignatura1)

# Agregar alumnos y asignaturas a la sesión
session.add(new_alumno1)
session.add(new_alumno2)
session.add(new_alumno3)
session.add(new_asignatura1)
session.add(new_asignatura2)
session.add(new_asignatura3)
session.add(new_asignatura4)
session.add(new_asignatura5)


# Confirmar la sesión
session.commit()
session.close()
