# Importo las herramientas que necesito de Pydantic
from pydantic import BaseModel, EmailStr, Field

# Importo datetime para manejar fechas
from datetime import datetime

# Importo Optional por si después necesito campos opcionales
from typing import Optional


# Creo el modelo base que tendrá la información principal del usuario
class UsuarioBase(BaseModel):

    # Guardo el correo y valido que tenga formato de email
    email: EmailStr

    # Defino el username con un mínimo y máximo de caracteres
    username: str = Field(min_length=5, max_length=15)

    # Asigno un rol por defecto
    role: str = "aprendiz"


# Creo el modelo para registrar usuarios
class UsuarioCrear(UsuarioBase):

    # Defino la contraseña con mínimo 10 caracteres
    password: str = Field(
        min_length=10,
        json_schema_extra={"example": "Segura123456"}
    )


# Creo el modelo que usaré para mostrar datos del usuario
class UsuarioSalida(UsuarioBase):

    # Agrego el id del usuario
    id: int

    # Agrego la fecha de creación
    created_at: datetime


    # Configuro el modelo para que pueda leer datos desde objetos
    class Config:
        from_attributes = True