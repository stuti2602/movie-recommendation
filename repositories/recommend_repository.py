from config.db import db
from bson import ObjectId

movies_collection = db.get_collection("movies")
users_collection = db.get_collection("users")

async def get_user_preferences_and_watchlist(user_id: str):
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        return None
    return {
        "preferences": user.get("preferences", []),
        "watchlist": user.get("movies_watchlist", [])
    }

async def get_movies_by_preferences(preferences: list, exclude_ids: list):
    query = {
        "genre": {"$in": preferences},
        "_id": {"$nin": [ObjectId(mid) if isinstance(mid, str) and len(mid) == 24 else mid for mid in exclude_ids]}
    }
    cursor = movies_collection.find(query).sort("rating", -1)
    return await cursor.to_list(length=5)