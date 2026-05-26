# Importo BaseModel y Field desde Pydantic
from pydantic import BaseModel, Field


# Creo el modelo base para los productos
class ProductoBase(BaseModel):
    # Defino el nombre del producto con mínimo y máximo de caracteres
    nombre: str = Field(min_length=2, max_length=100)
    # Defino el stock y evito números negativos
    stock: int = Field(ge=0)
    # Defino el precio y obligo que sea mayor a 0
    precio: float = Field(gt=0)


# Creo el modelo para registrar productos
class ProductoCrear(ProductoBase):
    # Uso los mismos campos del modelo base
    pass


# Creo el modelo para mostrar productos
class ProductoSalida(ProductoBase):
    # Agrego el id del producto
    id: int

    # Permito leer datos desde objetos
    class Config:
        from_attributes = True
