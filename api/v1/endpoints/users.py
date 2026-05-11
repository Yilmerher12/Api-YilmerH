from typing import List
from datetime import datetime
from fastapi import APIRouter, status, HTTPException
from schemes.user import UserCreate, UserOut, UserUpdate

# Base de datos simulada
usuarios_db = [
    {"id": 1, "email": "profe@sena.edu.co", "username": "profe_jenn", "role": "instructor", "created_at": datetime.now()}
]

router = APIRouter()

@router.get("/", response_model=List[UserOut])
async def obtener_usuarios():
    return usuarios_db

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def crear_usuario(user_in: UserCreate):
    nuevo_id = max(u["id"] for u in usuarios_db) + 1 if usuarios_db else 1
    nuevo_usuario = {
        **user_in.model_dump(),
        "id": nuevo_id,
        "created_at": datetime.now()
    }
    usuarios_db.append(nuevo_usuario)
    return nuevo_usuario

@router.put("/{id}", response_model=UserOut)
async def actualizar_usuario(id: int, user_in: UserUpdate):
    for i, u in enumerate(usuarios_db):
        if u["id"] == id:
            # exclude_unset=True evita que los campos que no enviaste sobrescriban con Nulo
            datos_actualizados = user_in.model_dump(exclude_unset=True)
            usuarios_db[i].update(datos_actualizados)
            return usuarios_db[i]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(id: int):
    for i, u in enumerate(usuarios_db):
        if u["id"] == id:
            usuarios_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Usuario no encontrado")