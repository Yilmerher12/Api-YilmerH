# Importo APIRouter para organizar las rutas de la API
from fastapi import APIRouter
from api.v1.endpoints import usuarios
from api.v1.endpoints import productos


# Creo un router principal para agrupar las rutas
api_router = APIRouter()


# Agrego las rutas relacionadas con usuarios
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])

# Agrego las rutas relacionadas con productos
api_router.include_router(productos.router, prefix="/productos",tags=["Productos"]
)