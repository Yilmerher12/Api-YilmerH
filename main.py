# vamos al entorno virtual, a la libreria fastapi y extraiga la clase principal FastAPI 
from fastapi import FastAPI
# Importamos el unificador maestro
from api.v1.api import api_router

#vEsta variable 'app' es la aplicación central que gestionará todas las rutas y configuraciones de tu API.
app = FastAPI()

# Fusionamos el unificador maestro a la memoria central de la aplicación
app.include_router(api_router)


# Decorador de operación de ruta.
# Le indica a la aplicación ('app') que cuando reciba una petición HTTP de tipo GET en la ruta inicial ("/"), debe ejecutar específicamente la función que se define justo debajo.
@app.get("/")


#'async' define que esta es una función asincrónica. Esto significa que si la función necesita esperar un proceso (como consultar una base de datos), el servidor no se detiene; cede el control para atender otras peticiones al mismo tiempo.
async def root():
# Retorna un diccionario estándar de Python.
# FastAPI se encarga automáticamente de tomar este diccionario y convertirlo (serializarlo) a formato JSON para que el sistema que hizo la petición pueda entender la respuesta.
    return {"mensaje": "Hola FastAPI"}