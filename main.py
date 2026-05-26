# Importo FastAPI para poder crear mi aplicación web
from fastapi import FastAPI
from api.v1.endpoints import usuarios
from api.v1.endpoints import productos

# Creo mi aplicación principal y le doy un título
app = FastAPI(title="VerdeApp API")


# Agrego las rutas relacionadas con usuarios
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])

# Agrego las rutas relacionadas con productos
app.include_router(productos.router, prefix="/api/productos", tags=["Productos"])


# Creo una ruta principal para comprobar si el servidor funciona
@app.get("/")

# Defino una función asíncrona que se ejecuta cuando entro a la ruta "/"
async def estado_servidor():
    return {"mensaje": "El servidor de VerdeApp está en línea y funcionando"}
