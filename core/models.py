# Importo los tipos de columnas que usaré, el uso del tipo de dato fecha y la clase database.pý 
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from core.database import Base


# Creo el modelo de usuarios
class UsuarioDB(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    username = Column(String(15))
    role = Column(String(20), default="aprendiz")
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Indico si el usuario está activo
    activo = Column(Boolean, default=True)


# Creo el modelo de productos
class ProductoDB(Base):

    # Defino el nombre de la tabla
    __tablename__ = "productos"


    # Creo el id como llave principal
    id = Column(Integer, primary_key=True, index=True)

    # Creo la columna del nombre del producto
    nombre = Column(String(100), unique=True)

    # Creo la columna del stock
    stock = Column(Integer)

    # Creo la columna del precio
    precio = Column(Float)

    # Indico si el producto está activo
    activo = Column(Boolean, default=True)
