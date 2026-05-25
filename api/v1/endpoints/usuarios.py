# clase que se encuentra en la libreria fastapi
# Nos ayudara a crear los endpoints de cualquier modulo o recurso del proyecto
from fastapi import APIRouter
from pydantic import BaseModel

# Creamos la instancia del enrutador para este módulo
router = APIRouter()

class UsuarioCrear(BaseModel):
    nombre: str
    email: int
    password: str

# Registramos el endpoint en este router específico
@router.get("/")
async def obtener_usuarios():
    return {"mensaje": "Aquí se devolverán las filas de usuarios"}

@router.post("/crear")
async def crear_usuario(usuario: UsuarioCrear):
    return {"mensaje": "Registro validado correctamente", "datos": usuario}