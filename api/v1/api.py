from fastapi import APIRouter
# Importamos el archivo de usuarios que acabamos de crear
from api.v1.endpoints import usuarios

# Creamos el enrutador maestro
api_router = APIRouter()

# Fusionamos las rutas de usuarios dentro del maestro
api_router.include_router(usuarios.router, prefix="/usuarios")