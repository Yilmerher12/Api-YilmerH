# Importo herramientas de FastAPI
from fastapi import APIRouter, Depends, HTTPException, status

# Importo Session para trabajar con la base de datos
from sqlalchemy.orm import Session

# Importo la función para conectarme a la base de datos
from core.database import get_db

# Importo el modelo de productos
from core.models import ProductoDB

# Importo los esquemas de productos
from schemas.producto import ProductoCrear, ProductoSalida


# Creo el router para las rutas de productos
router = APIRouter()


# Creo una ruta POST para registrar productos
@router.post(
    "/crear",
    response_model=ProductoSalida,
    status_code=status.HTTP_201_CREATED
)
async def crear_producto(
    producto: ProductoCrear,
    db: Session = Depends(get_db)
):

    # Busco si ya existe un producto con el mismo nombre
    registro_existente = (
        db.query(ProductoDB)
        .filter(ProductoDB.nombre == producto.nombre)
        .first()
    )


    # Verifico si el producto ya está registrado
    if registro_existente:

        # Envío un error si el producto ya existe
        raise HTTPException(
            status_code=400,
            detail="El producto ya está registrado"
        )


    # Creo un nuevo producto con los datos recibidos
    nuevo_registro = ProductoDB(
        nombre=producto.nombre,
        stock=producto.stock,
        precio=producto.precio
    )


    # Agrego el producto a la sesión
    db.add(nuevo_registro)

    # Guardo los cambios en la base de datos
    db.commit()

    # Actualizo los datos del producto creado
    db.refresh(nuevo_registro)


    # Retorno el producto creado
    return nuevo_registro


# Creo una ruta DELETE para desactivar productos
@router.delete("/eliminar/{producto_id}")
async def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):

    # Busco el producto por su id
    registro_a_eliminar = (
        db.query(ProductoDB)
        .filter(ProductoDB.id == producto_id)
        .first()
    )


    # Verifico si el producto existe
    if registro_a_eliminar is None:

        # Envío un error si el producto no existe
        raise HTTPException(
            status_code=404,
            detail="El registro solicitado no existe"
        )


    # Cambio el estado del producto a inactivo
    registro_a_eliminar.activo = False


    # Guardo los cambios
    db.commit()


    # Retorno un mensaje de confirmación
    return {
        "mensaje": "El producto ha sido desactivado permanentemente (Borrado lógico)"
    }
