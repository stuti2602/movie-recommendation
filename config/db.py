from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_DB_URL") # Check Variable Name in ENV File
DB_NAME = os.getenv("MONGO_DB_NAME") # Check Variable Name in ENV File

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
movies_collection = db.get_collection("movies")