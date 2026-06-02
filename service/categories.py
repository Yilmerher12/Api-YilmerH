from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.categorias_db import CategoriaDB
from schemas.categoria import CategoriaCrear, CategoriaActualizar


class CategoryService:
    """Service para operaciones CRUD de categorías."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(CategoriaDB).filter(CategoriaDB.activo == True).all()

    def get_by_id(self, cat_id: int):
        return self.db.query(CategoriaDB).filter(CategoriaDB.id == cat_id, CategoriaDB.activo == True).first()

    def create(self, cat_in: CategoriaCrear):
        data = cat_in.model_dump()
        # Validar nombre único
        if self.db.query(CategoriaDB).filter(CategoriaDB.nombre == data.get("nombre"), CategoriaDB.activo == True).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de la categoría ya existe")

        db_cat = CategoriaDB(**data)
        self.db.add(db_cat)
        self.db.commit()
        self.db.refresh(db_cat)
        return db_cat

    def update(self, cat_id: int, cat_in: CategoriaActualizar):
        db_cat = self.get_by_id(cat_id)
        if not db_cat:
            return None
        update_data = cat_in.model_dump(exclude_unset=True)
        if "nombre" in update_data:
            existe = self.db.query(CategoriaDB).filter(CategoriaDB.nombre == update_data["nombre"], CategoriaDB.id != cat_id, CategoriaDB.activo == True).first()
            if existe:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de la categoría ya existe")

        for key, value in update_data.items():
            setattr(db_cat, key, value)
        self.db.commit()
        self.db.refresh(db_cat)
        return db_cat

    def delete(self, cat_id: int):
        db_cat = self.get_by_id(cat_id)
        if db_cat:
            db_cat.activo = False
            self.db.add(db_cat)
            self.db.commit()
            return True
        return False
