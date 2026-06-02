from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.users_db import UsuarioDB
from schemas.usuario import UsuarioCrear, UsuarioUpdate


class UserService:
    """Agrupa las operaciones CRUD de usuarios sobre una sesión de BD."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        # Solo devolver usuarios activos
        return self.db.query(UsuarioDB).filter(UsuarioDB.activo == True).all()

    def get_by_id(self, user_id: int):
        # Obtener solo si está activo
        return self.db.query(UsuarioDB).filter(UsuarioDB.id == user_id, UsuarioDB.activo == True).first()

    def create(self, user_in: UsuarioCrear):
        data = user_in.model_dump()

        # Validar duplicados: email y username únicos entre activos
        if self.db.query(UsuarioDB).filter(UsuarioDB.email == data.get("email"), UsuarioDB.activo == True).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")
        if self.db.query(UsuarioDB).filter(UsuarioDB.username == data.get("username"), UsuarioDB.activo == True).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El username ya está registrado")

        db_user = UsuarioDB(**data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user_in: UsuarioUpdate):
        db_user = self.get_by_id(user_id)
        if db_user:
            update_data = user_in.model_dump(exclude_unset=True)

            # Si cambia email o username, verificar duplicados en otros registros activos
            if "email" in update_data:
                existe = self.db.query(UsuarioDB).filter(UsuarioDB.email == update_data["email"], UsuarioDB.id != user_id, UsuarioDB.activo == True).first()
                if existe:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")
            if "username" in update_data:
                existe2 = self.db.query(UsuarioDB).filter(UsuarioDB.username == update_data["username"], UsuarioDB.id != user_id, UsuarioDB.activo == True).first()
                if existe2:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El username ya está registrado")

            for key, value in update_data.items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int):
        # Soft delete: marcar activo = False
        db_user = self.get_by_id(user_id)
        if db_user:
            db_user.activo = False
            self.db.add(db_user)
            self.db.commit()
            return True
        return False
 