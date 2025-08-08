from config.db import db

users_collection = db.get_collection("users")
movies_collection = db.get_collection("movies")


async def get_user_by_email(user_email: str):
    return await users_collection.find_one({"email": user_email})


async def get_movies_by_titles(titles: list):
    if not isinstance(titles, list):
        titles = [titles]
    cursor = movies_collection.find({"title": {"$in": titles}})
    return await cursor.to_list(length=len(titles))


async def get_movie_by_title(movie_title: str):
    return await movies_collection.find_one({"title": movie_title})


async def get_movie_by_id(movie_id: int):
    return await movies_collection.find_one({"_id": movie_id})


async def add_movie_title_to_user_watchlist_by_email(user_email: str, movie_title: str):
    result = await users_collection.update_one(
        {"email": user_email},
        {"$addToSet": {"movies_watchlist": movie_title}}  # prevents duplicates
    )
    return result.modified_count > 0



async def remove_movie_title_from_user_watchlist_by_email(user_email: str, movie_title: str):
    result = await users_collection.update_one(
        {"email": user_email},
        {"$pull": {"movies_watchlist": movie_title}}
    )
    # result.modified_count > 0 means something was actually removed
    return result.modified_count > 0
