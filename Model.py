from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class User(Base):
    __tablemane__= 'user'

    id= Column(Integer, primary_key=True)
    Objetivo_inversion= Column(String(50))
    Ocupacion=Column(String(50))
    Grado_estudio= Column(String(50))
    Cantidad_de_inversion= Column(Float)
    Provenencia_del_dinero= Column(String(50))
    Tiempo_de_inversion= Column(int)



