from typing import List

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from models import users_db
from schemas.usuario import UsuarioCrear, UsuarioUpdate, UsuarioSalida
from service.users import UserService

router = APIRouter()


@router.get("/", response_model=List[UsuarioSalida])
def obtener_usuarios(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all()


@router.get("/{id}", response_model=UsuarioSalida)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    usuario = service.get_by_id(id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.post("/", response_model=UsuarioSalida, status_code=status.HTTP_201_CREATED)
def crear_usuario(nuevo: UsuarioCrear, db: Session = Depends(get_db)):
    service = UserService(db)
    usuario = service.create(nuevo)
    return usuario


@router.put("/{id}", response_model=UsuarioSalida)
def actualizar_usuario(id: int, datos: UsuarioUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    usuario = service.update(id, datos)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    exito = service.delete(id)
    if not exito:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return

