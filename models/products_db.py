# Importo los tipos de columnas que usaré, el uso del tipo de dato fecha y la clase database.pý 
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from core.database import Base

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
    
    # Llave foránea a categoría
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    # Relación con la categoría
    categoria = relationship("CategoriaDB", back_populates="productos")
