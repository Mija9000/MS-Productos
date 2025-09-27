from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ms_productos.routes import router as product_router

app = FastAPI(
    title="MS Productos",
    description="Microservicio de productos para ecommerce",
    version="1.0"
)

# Configuración CORS solo para tu front
origins = [
    "https://main.dqd6rclpd8bw6.amplifyapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router, prefix="/productos", tags=["Productos"])

@app.get("/")
async def root():
    return {"message": "Microservicio de productos funcionando!"}
