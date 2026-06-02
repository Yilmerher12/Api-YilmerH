from fastapi import APIRouter
from api.v1.endpoints import productos, usuarios, categorias


api_router = APIRouter()

# Agrego los routers de los recursos aquí
api_router.include_router(productos.router, prefix="/productos", tags=["productos"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
api_router.include_router(categorias.router, prefix="/categorias", tags=["categorias"])