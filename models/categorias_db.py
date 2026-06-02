from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from core.database import Base
# Modelo de categorías
class CategoriaDB(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    descripcion = Column(String(255), nullable=True)
    creado_en = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)

    # Relación con productos
    productos = relationship("ProductoDB", back_populates="categoria")
