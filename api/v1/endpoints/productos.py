from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Importamos la infraestructura
from core.database import get_db
from models import products_db
from schemas.producto import ProductoCrear, ProductoUpdate, ProductoSalida
from service.products import ProductService

router = APIRouter()


@router.get("/", response_model=List[ProductoSalida])
def obtener_productos(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all()


@router.get("/{id}", response_model=ProductoSalida)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    producto = service.get_by_id(id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return producto


@router.post("/", response_model=ProductoSalida, status_code=status.HTTP_201_CREATED)
def crear_producto(new_product: ProductoCrear, db: Session = Depends(get_db)):
    service = ProductService(db)
    producto_creado = service.create(new_product)
    return producto_creado


@router.put("/{id}", response_model=ProductoSalida)
def actualizar_producto(id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    service = ProductService(db)
    producto_actualizado = service.update(id, producto)
    if not producto_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return producto_actualizado


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    exito = service.delete(id)
    if not exito:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return