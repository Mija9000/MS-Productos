from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ms_productos.routes import router as product_router  # tu router de productos

app = FastAPI()

# Configuración CORS
origins = [
    "*",  # durante pruebas puedes permitir todo
    # luego puedes restringir: "https://tu-frontend.amplifyapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, PUT, DELETE, etc
    allow_headers=["*"],         # qué headers se aceptan
)

# Incluimos las rutas
app.include_router(product_router)
