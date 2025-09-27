import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "ecommerce_db")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
collection_productos = db["productos"]
