from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.categoria import CategoriaCrear, CategoriaActualizar, CategoriaSalida
from service.categories import CategoryService

router = APIRouter()


@router.get("/", response_model=List[CategoriaSalida])
def obtener_categorias(db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_all()


@router.get("/{id}", response_model=CategoriaSalida)
def obtener_categoria(id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    categoria = service.get_by_id(id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return categoria


@router.post("/", response_model=CategoriaSalida, status_code=status.HTTP_201_CREATED)
def crear_categoria(nueva: CategoriaCrear, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.create(nueva)


@router.put("/{id}", response_model=CategoriaSalida)
def actualizar_categoria(id: int, datos: CategoriaActualizar, db: Session = Depends(get_db)):
    service = CategoryService(db)
    categoria = service.update(id, datos)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return categoria


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    exito = service.delete(id)
    if not exito:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return
