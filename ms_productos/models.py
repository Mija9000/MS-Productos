from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int
    imageUrl: Optional[str] = None

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    imageUrl: Optional[str] = None
