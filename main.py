#1. Importar fast api
from fastapi import FastAPI
from api.v1.api import api_router 

#2. Crear instancia de fastapi
app =FastAPI(
    title="Mi primera API FAST API",
    description="Primera API con fast API por Yilmer Hernandez Camargo",
    version="1.0.0",
    
)

# Conexión de todas las rutas bajo el prefijo /api/v1
app.include_router(api_router, prefix="/api/v1")

#3. Definir un endpoint en la ruta raiz
@app.get("/")
async def root():
    return {"message": "Hola jejej desde FastAPI!"}
