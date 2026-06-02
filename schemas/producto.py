# Importo BaseModel y Field desde Pydantic
from pydantic import BaseModel, Field
from typing import Optional


# Creo el modelo base para los productos
class ProductoBase(BaseModel):
    # Defino el nombre del producto con mínimo y máximo de caracteres
    nombre: str = Field(min_length=2, max_length=100)
    # Defino el stock y evito números negativos
    stock: int = Field(ge=0)
    # Defino el precio y obligo que sea mayor a 0
    precio: float = Field(gt=0)
    # Relación a categoría (id)
    categoria_id: int = Field(gt=0)


# Creo el modelo para registrar productos
class ProductoCrear(ProductoBase):
    # Uso los mismos campos del modelo base
    pass


# Modelo para actualizaciones parciales (campos opcionales)
class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    stock: Optional[int] = Field(None, ge=0)
    precio: Optional[float] = Field(None, gt=0)
    categoria_id: Optional[int] = Field(None, gt=0)


# Creo el modelo para mostrar productos
class ProductoSalida(ProductoBase):
    # Agrego el id del producto
    id: int
    categoria_id: int

    # Permito leer datos desde objetos
    class Config:
        from_attributes = True
