from bson import ObjectId
from config.db import db

users_collection = db.get_collection("users")
movies_collection = db.get_collection("movies")


async def get_user_by_id(user_id: str):
    return await users_collection.find_one({"_id": ObjectId(user_id)})


async def get_movies_by_ids(movie_ids: list):
    cursor = movies_collection.find({"_id": {"$in": movie_ids}})
    return await cursor.to_list(length=len(movie_ids))


async def get_movie_by_id(movie_id: int):
    return await movies_collection.find_one({"_id": movie_id})


async def add_movie_id_to_user_watchlist(user_id: str, movie_id: int):
    result = await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"movies_watchlist": movie_id}}  # prevent duplicates
    )
    return result.modified_count > 0


async def remove_movie_id_from_user_watchlist(user_id: str, movie_id: int):
    result = await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$pull": {"movies_watchlist": movie_id}}
    )
    return result.modified_count > 0
