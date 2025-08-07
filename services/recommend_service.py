from fastapi import HTTPException
import repositories.recommend_repository as repo

async def get_recommendations(user_id: str):
    data = await repo.get_user_preferences_and_watchlist(user_id)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
   
    preferences = data["preferences"]
    watchlist = data["watchlist"]
   
    if not preferences:
        raise HTTPException(status_code=400, detail="User has no preferences set")

    movies = await repo.get_movies_by_preferences(preferences, watchlist)

    return [
        {
            "id": str(movie["_id"]),
            "title": movie["title"],
            "description": movie["description"],
            "genre": movie["genre"],
            "rating": movie["rating"]
        }
        for movie in movies
    ]
