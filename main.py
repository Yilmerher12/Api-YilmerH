# Importo FastAPI para poder crear mi aplicación web
from fastapi import FastAPI

# Importo el archivo de endpoints de usuarios
from api.endpoints import usuarios

# Importo el archivo de endpoints de productos
from api.endpoints import productos


# Creo mi aplicación principal y le doy un título
app = FastAPI(title="VerdeApp API")


# Agrego las rutas relacionadas con usuarios
app.include_router(
    usuarios.router,                 # Uso el router que está en el archivo de usuarios
    prefix="/api/usuarios",          # Defino el prefijo que tendrán las rutas de usuarios
    tags=["Usuarios"]                # Coloco una etiqueta para organizar la documentación
)

# Agrego las rutas relacionadas con productos
app.include_router(
    productos.router,                # Uso el router que está en el archivo de productos
    prefix="/api/productos",         # Defino el prefijo que tendrán las rutas de productos
    tags=["Productos"]               # Coloco una etiqueta para organizar la documentación
)


# Creo una ruta principal para comprobar si el servidor funciona
@app.get("/")

# Defino una función asíncrona que se ejecuta cuando entro a la ruta "/"
async def estado_servidor():

    # Retorno un mensaje indicando que el servidor está funcionando
    return {"mensaje": "El servidor de VerdeApp está en línea y funcionando"}
