from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ms_productos.routes import router as product_router

app = FastAPI()

# Configuración CORS
origins = ["*"]  # en producción deberías restringirlo

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluimos las rutas
app.include_router(product_router, prefix="/productos", tags=["Productos"])
