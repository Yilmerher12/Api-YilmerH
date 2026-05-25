# Importo herramientas de FastAPI
from fastapi import APIRouter, Depends, HTTPException, status

# Importo Session para trabajar con la base de datos
from sqlalchemy.orm import Session

# Importo la función que me da acceso a la base de datos
from core.database import get_db

# Importo el modelo de usuarios de la base de datos
from core.models import UsuarioDB

# Importo los esquemas de entrada y salida
from schemas.usuario import UsuarioCrear, UsuarioSalida


# Creo el router para las rutas de usuarios
router = APIRouter()


# Creo una ruta POST para registrar usuarios
@router.post(
    "/crear",
    response_model=UsuarioSalida,
    status_code=status.HTTP_201_CREATED
)
async def crear_usuario(
    usuario: UsuarioCrear,
    db: Session = Depends(get_db)
):

    # Busco si ya existe un usuario con el mismo correo
    registro_existente = (
        db.query(UsuarioDB)
        .filter(UsuarioDB.email == usuario.email)
        .first()
    )


    # Verifico si el correo ya está registrado
    if registro_existente:

        # Envío un error si el correo ya existe
        raise HTTPException(
            status_code=400,
            detail="El correo ya esta registrado"
        )


    # Creo un nuevo usuario con los datos recibidos
    nuevo_registro = UsuarioDB(
        email=usuario.email,
        username=usuario.username,
        role=usuario.role,
        password=usuario.password
    )


    # Agrego el nuevo usuario a la sesión
    db.add(nuevo_registro)

    # Guardo los cambios en la base de datos
    db.commit()

    # Actualizo los datos del nuevo usuario
    db.refresh(nuevo_registro)


    # Retorno el usuario creado
    return nuevo_registro


# Creo una ruta DELETE para desactivar usuarios
@router.delete("/eliminar/{usuario_id}")
async def eliminar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):

    # Busco el usuario por su id
    registro_a_eliminar = (
        db.query(UsuarioDB)
        .filter(UsuarioDB.id == usuario_id)
        .first()
    )


    # Verifico si el usuario existe
    if registro_a_eliminar is None:

        # Envío un error si el usuario no existe
        raise HTTPException(
            status_code=404,
            detail="El registro solicitado no existe"
        )


    # Cambio el estado del usuario a inactivo
    registro_a_eliminar.activo = False


    # Guardo los cambios
    db.commit()


    # Retorno un mensaje de confirmación
    return {
        "mensaje": "El usuario ha sido desactivado permanentemente (Borrado lógico)"
    }
