from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="yilmer@correo.com")
    username: str = Field(..., min_length=5, max_length=15, example="yilmer_dev")
    role: Optional[str] = Field("aprendiz", example="aprendiz")

class UserCreate(UserBase):
    password: str = Field(..., min_length=10, example="ClaveSegura123")

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(None, example="nuevo@correo.com")
    username: Optional[str] = Field(None, min_length=5, max_length=15)
    password: Optional[str] = Field(None, min_length=10)
    role: Optional[str] = Field(None)

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True