from fastapi import APIRouter
from api.v1.endpoints import products, users # Importamos el nuevo archivo

api_router = APIRouter()

# Conectamos productos
api_router.include_router(products.router, prefix="/products", tags=["Productos"])

# Conectamos usuarios
api_router.include_router(users.router, prefix="/users", tags=["Usuarios"])