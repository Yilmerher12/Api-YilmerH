from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.products_db import ProductoDB
from models.categorias_db import CategoriaDB
from schemas.producto import ProductoCrear, ProductoUpdate


class ProductService:
    """Agrupa las operaciones CRUD de productos sobre una sesión de BD."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        # Solo devolver productos activos (soft-delete)
        return self.db.query(ProductoDB).filter(ProductoDB.activo == True).all()

    def get_by_id(self, product_id: int):
        # Solo obtener producto si está activo
        return self.db.query(ProductoDB).filter(ProductoDB.id == product_id, ProductoDB.activo == True).first()

    def create(self, product_in: ProductoCrear):
        data = product_in.model_dump()

        # Validaciones de integridad
        if data.get("stock", 0) < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Stock no puede ser negativo")
        if data.get("precio", 0) <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El precio debe ser mayor que 0")

        # Evitar duplicados por nombre (solo entre activos)
        existente = self.db.query(ProductoDB).filter(ProductoDB.nombre == data.get("nombre"), ProductoDB.activo == True).first()
        if existente:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del producto ya está registrado")

        # Verificar que la categoría exista y esté activa
        categoria_id = data.get("categoria_id")
        categoria = self.db.query(CategoriaDB).filter(CategoriaDB.id == categoria_id, CategoriaDB.activo == True).first()
        if not categoria:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoría indicada no existe o no está activa")

        db_product = ProductoDB(**data)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update(self, product_id: int, product_in: ProductoUpdate):
        db_product = self.get_by_id(product_id)
        if db_product:
            update_data = product_in.model_dump(exclude_unset=True)

            # Validaciones si se envían
            if "stock" in update_data and update_data["stock"] < 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Stock no puede ser negativo")
            if "precio" in update_data and update_data["precio"] <= 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El precio debe ser mayor que 0")

            # Si cambia el nombre, verificar duplicado en otros registros activos
            if "nombre" in update_data:
                existe = self.db.query(ProductoDB).filter(ProductoDB.nombre == update_data["nombre"], ProductoDB.id != product_id, ProductoDB.activo == True).first()
                if existe:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del producto ya está registrado")

            # Si cambia categoría, validar que exista y esté activa
            if "categoria_id" in update_data:
                cat = self.db.query(CategoriaDB).filter(CategoriaDB.id == update_data["categoria_id"], CategoriaDB.activo == True).first()
                if not cat:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoría indicada no existe o no está activa")

            for key, value in update_data.items():
                setattr(db_product, key, value)
            self.db.commit()
            self.db.refresh(db_product)
        return db_product

    def delete(self, product_id: int):
        # Soft delete: marcar activo = False
        db_product = self.get_by_id(product_id)
        if db_product:
            db_product.activo = False
            self.db.add(db_product)
            self.db.commit()
            return True
        return False
