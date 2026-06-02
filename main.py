# Importo FastAPI para poder crear mi aplicación web
from fastapi import FastAPI, APIRouter
from api.v1.endpoints import productos, usuarios, categorias

from core.database import Base, engine, SessionLocal
from service.categories import CategoryService
from schemas.categoria import CategoriaCrear
from service.products import ProductService
from schemas.producto import ProductoCrear


# Creo mi aplicación principal y le doy un título
app = FastAPI(title="VerdeApp API")

# Creo el router para incluir las rutas
api_router = APIRouter()

# Incluyo el router de productos bajo /productos
api_router.include_router(productos.router, prefix="/productos", tags=["productos"])
# Incluyo el router de usuarios bajo /usuarios
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
# Incluyo el router de categorias bajo /categorias
api_router.include_router(categorias.router, prefix="/categorias", tags=["categorias"])

# Conexión de todas las rutas bajo el prefijo /api/v1
app.include_router(api_router, prefix="/api/v1")


# Creo las tablas en la base de datos (si no existen). Si no hay configuración
# de base de datos, ignoramos este paso para permitir desarrollo sin BD.
if engine is not None:
    try:
        Base.metadata.create_all(bind=engine)

        # Seed inicial de categorías (solo si no hay ninguna)
        db = SessionLocal()
        try:
            service = CategoryService(db)
            existentes = service.get_all()
            if not existentes:
                defaults = [
                    {"nombre": "Papelería", "descripcion": "Útiles de escritura y oficina"},
                    {"nombre": "Tecnología", "descripcion": "Accesorios y dispositivos electrónicos"},
                    {"nombre": "Hogar", "descripcion": "Artículos para el hogar"},
                    {"nombre": "Ropa", "descripcion": "Prendas de vestir"},
                    {"nombre": "Alimentos", "descripcion": "Productos comestibles"},
                ]
                for c in defaults:
                    try:
                        service.create(CategoriaCrear(**c))
                    except Exception:
                        # si hay algún conflicto se ignora
                        pass
                # Seed inicial de productos (si no hay ninguno)
                product_service = ProductService(db)
                existentes_p = product_service.get_all()
                if not existentes_p:
                    # crear productos asociados a las categorías creadas
                    categorias = service.get_all()
                    cat_map = {c.nombre: c.id for c in categorias}
                    defaults_p = [
                        {"nombre": "Cuaderno A5", "stock": 50, "precio": 3.5, "categoria_id": cat_map.get("Papelería")},
                        {"nombre": "Bolígrafo Azul", "stock": 200, "precio": 0.8, "categoria_id": cat_map.get("Papelería")},
                        {"nombre": "Mouse Inalámbrico", "stock": 30, "precio": 15.0, "categoria_id": cat_map.get("Tecnología")},
                        {"nombre": "Cargador USB-C", "stock": 40, "precio": 12.0, "categoria_id": cat_map.get("Tecnología")},
                        {"nombre": "Juego de Sábanas", "stock": 20, "precio": 25.0, "categoria_id": cat_map.get("Hogar")},
                        {"nombre": "Camiseta Algodón", "stock": 100, "precio": 10.0, "categoria_id": cat_map.get("Ropa")},
                        {"nombre": "Pantalón Jeans", "stock": 60, "precio": 20.0, "categoria_id": cat_map.get("Ropa")},
                        {"nombre": "Arroz 1kg", "stock": 300, "precio": 1.2, "categoria_id": cat_map.get("Alimentos")},
                        {"nombre": "Aceite 1L", "stock": 150, "precio": 4.0, "categoria_id": cat_map.get("Alimentos")},
                        {"nombre": "Lámpara de Mesa", "stock": 25, "precio": 18.0, "categoria_id": cat_map.get("Hogar")},
                    ]
                    for p in defaults_p:
                        try:
                            product_service.create(ProductoCrear(**p))
                        except Exception:
                            pass
        finally:
            db.close()
    except Exception as e:
        # No interrumpir el arranque de la app si la BD no está accesible
        print("Advertencia: no se pudieron crear las tablas en la base de datos:", str(e))
else:
    print("Advertencia: la base de datos no está configurada. Defina DB_USER/DB_NAME en .env para habilitarla.")


# Creo una ruta principal para comprobar si el servidor funciona
@app.get("/")
async def estado_servidor():
    return {"mensaje": "El servidor de VerdeApp está en línea y funcionando"}
