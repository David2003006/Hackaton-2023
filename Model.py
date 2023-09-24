from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class User(Base):
    __tablename__ = 'user'

    id= Column(Integer, primary_key=True, autoincrement=True, unique=True)
    plazo = Column(Integer)

class Fondo_Inversion(Base):
    __tablename__= 'fondo_Inversion'

    id= Column(Integer, primary_key=True,autoincrement=True, unique=True)
    nombre= Column(String(50))
    puntaje= Column(Float)
    fecha= Column(Date)

class Noticia(Base):
    __tablename__ = 'Noticia'

    id = Column(Integer, primary_key=True, unique=True)
    titulo = Column(String(50))
    categoria = Column(String(50))
    tipo_de_fondo = Column(Integer, ForeignKey(Fondo_Inversion.id))  # Usar Integer en lugar de int
    contribucion = Column(Boolean)
    fecha = Column(Date)

class Respuestas_back(Base):
    __tablename__ = 'Respuest_back'

    user_id = Column(Integer, ForeignKey(User.id), primary_key=True, unique=True)
    role = relationship('Respuesta', back_populates='users')
    fondo_recomendado = Column(Integer, ForeignKey(Fondo_Inversion.id))
    fecha = Column(Date)