from fastapi import APIRouter
from ms_productos.models import Producto
from ms_productos.database import productos_collection

router = APIRouter()

@router.get("/productos", response_model=list[Producto])
def get_productos():
    return list(productos_collection.find({}, {"_id": 0}))

@router.get("/productos/{id}", response_model=Producto)
def get_producto(id: int):
    return productos_collection.find_one({"id": id}, {"_id": 0})
