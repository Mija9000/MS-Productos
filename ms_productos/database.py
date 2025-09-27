from pymongo import MongoClient

# Conexión a MongoDB (por ahora en localhost)
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]   # nombre de la base
productos_collection = db["productos"]
