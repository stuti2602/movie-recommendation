from fastapi import HTTPException
import repositories.watchlist_repository as repo

async def add_movie_to_watchlist_by_email(user_email: str, movie_title: str):
    # Check if movie exists in movies_collection
    movie = await repo.get_movie_by_title(movie_title)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    # Add movie title to watchlist
    updated = await repo.add_movie_title_to_user_watchlist_by_email(user_email, movie_title)
    if not updated:
        raise HTTPException(status_code=400, detail="Movie already in watchlist")

    return {"message": f'"{movie_title}" added to watchlist'}


async def get_watchlist_by_email(user_email: str):
    user = await repo.get_user_by_email(user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    movie_titles = user.get("movies_watchlist", [])
    if not movie_titles:
        return {"watchlist": []}
    
    return {"watchlist": movie_titles}



async def remove_movie_from_watchlist_by_email(user_email: str, movie_title: str):
    # Try to remove movie from user's watchlist
    updated = await repo.remove_movie_title_from_user_watchlist_by_email(user_email, movie_title)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found in watchlist")
    
    return {"message": f'"{movie_title}" removed from watchlist'}

