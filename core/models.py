# Importo los tipos de columnas que usaré
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

# Importo datetime para manejar fechas
from datetime import datetime

# Importo la clase Base desde database.py
from core.database import Base


# Creo el modelo de usuarios
class UsuarioDB(Base):

    # Defino el nombre de la tabla
    __tablename__ = "usuarios"


    # Creo el id como llave principal
    id = Column(Integer, primary_key=True, index=True)

    # Creo la columna del email
    email = Column(String(100), unique=True, index=True)

    # Creo la columna del username
    username = Column(String(15))

    # Creo la columna del rol con un valor por defecto
    role = Column(String(20), default="aprendiz")

    # Creo la columna de la contraseña
    password = Column(String(255))

    # Guardo la fecha de creación automáticamente
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
