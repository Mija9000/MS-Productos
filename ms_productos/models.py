# ms_productos/models.py
from pydantic import BaseModel, Field
from typing import Optional

class Producto(BaseModel):
    id: Optional[str] = None
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: str = Field(..., min_length=1, max_length=300)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = Field(None, min_length=1, max_length=300)
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
