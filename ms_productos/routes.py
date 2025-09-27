from fastapi import APIRouter, HTTPException
from models.producto import Producto
from config.db import collection_productos

router = APIRouter()

# GET - Listar todos los productos
@router.get("/productos")
async def obtener_productos():
    productos = []
    async for producto in collection_productos.find():
        producto["_id"] = str(producto["_id"])
        productos.append(producto)
    return productos

# POST - Crear un producto nuevo
@router.post("/productos")
async def crear_producto(producto: Producto):
    nuevo = producto.model_dump()
    result = await collection_productos.insert_one(nuevo)
    if result.inserted_id:
        return {"_id": str(result.inserted_id), **nuevo}
    else:
        raise HTTPException(status_code=500, detail="No se pudo crear el producto")
