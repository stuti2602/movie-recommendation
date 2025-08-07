# config/db.py
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "movie_recommender")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

# Access collections
user_collection = db.get_collection("users")
movie_collection = db.get_collection("movies")
watchlist_collection = db.get_collection("user_watchlist")