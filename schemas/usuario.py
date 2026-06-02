# Importo BaseModel y Field desde Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr

# Creo el modelo base para los usuarios
class UsuarioBase(BaseModel):
    # Defino el username del usuario con mínimo y máximo de caracteres
    username: str = Field(min_length=2, max_length=100)
    # Defino el correo electrónico usando EmailStr para validación robusta
    email: EmailStr
    # Defino la contraseña con mínimo de caracteres
    password: str = Field(min_length=6, example="Contraseña123")
    
# Creo el modelo para registrar usuarios
class UsuarioCrear(UsuarioBase):
    # Uso los mismos campos del modelo base
    pass


# Modelo para actualizaciones parciales de usuario
from typing import Optional


class UsuarioUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)

# Creo el modelo para mostrar usuarios
class UsuarioSalida(UsuarioBase):
    # Agrego el id del usuario
    id: int

    # Permito leer datos desde objetos
    class Config:
        from_attributes = True  

