# repositories/user_repository.py
from config.db import db
from bson import ObjectId

users_collection = db.get_collection("users")
movies_collection = db.get_collection("movies")

async def find_by_email(email: str):
    return await users_collection.find_one({"email": email})

async def insert_user(user_data: dict):
    result = await users_collection.insert_one(user_data)
    return str(result.inserted_id)

async def get_user_by_id(user_id: str):
    return await users_collection.find_one({"_id": ObjectId(user_id)})

# ➕ Add to watchlist
async def add_movie_to_watchlist(user_id: str, movie_id: int):
    await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"movies_watchlist": movie_id}}
    )

# 📜 Get watchlist movies
async def get_watchlist_movies(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        return None
    movie_ids = user.get("movies_watchlist", [])
    if not movie_ids:
        return []
    cursor = movies_collection.find({"_id": {"$in": movie_ids}})
    return await cursor.to_list(length=None)

# ❌ Remove from watchlist
async def remove_movie_from_watchlist(user_id: str, movie_id: int):
    await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$pull": {"movies_watchlist": movie_id}}
    )
