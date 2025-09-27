from fastapi import APIRouter, HTTPException
from bson import ObjectId
from ms_productos.models import Producto, ProductoUpdate
from ms_productos.database import collection_productos

router = APIRouter()

# GET - Listar todos los productos
@router.get("/")
async def obtener_productos():
    productos = []
    async for producto in collection_productos.find():
        producto["_id"] = str(producto["_id"])
        productos.append(producto)
    return productos

# POST - Crear un producto nuevo
@router.post("/")
async def crear_producto(producto: Producto):
    nuevo = producto.model_dump()
    result = await collection_productos.insert_one(nuevo)
    if result.inserted_id:
        return {"_id": str(result.inserted_id), **nuevo}
    raise HTTPException(status_code=500, detail="No se pudo crear el producto")

# PUT - Actualizar un producto
@router.put("/{producto_id}")
async def actualizar_producto(producto_id: str, producto: ProductoUpdate):
    actualizacion = {k: v for k, v in producto.model_dump().items() if v is not None}

    if not actualizacion:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")

    result = await collection_productos.update_one(
        {"_id": ObjectId(producto_id)}, {"$set": actualizacion}
    )

    if result.modified_count == 1:
        actualizado = await collection_productos.find_one({"_id": ObjectId(producto_id)})
        actualizado["_id"] = str(actualizado["_id"])
        return actualizado
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# DELETE - Eliminar un producto
@router.delete("/{producto_id}")
async def eliminar_producto(producto_id: str):
    result = await collection_productos.delete_one({"_id": ObjectId(producto_id)})

    if result.deleted_count == 1:
        return {"message": "Producto eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
