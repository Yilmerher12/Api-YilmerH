# main.py
from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI(
    title="Mi Primera API por Yilmer Hernandez",
    description="API proyecto VerdeApp para SENA ",
    version="1.0.0",
)

@app.post("/saludo")
async def create_greeting(greeting: str):
    """Endpoint para crear un nuevo saludo."""
    if (greeting == "Yilmer"):
        return {"message": "Bienvenido a la app, Admin: "f"¡{greeting}!"}
    elif (greeting != "Yilmer" and greeting != ""):
        return {"message": "Bienvenido a la app, Usuario: "f"¡{greeting}!"}
    else:
        return {"message": "Lo siento, no tienes acceso a la app, Usuario: "f"¡{greeting}!"}