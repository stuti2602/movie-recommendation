from fastapi import HTTPException
import repositories.watchlist_repository as repo


async def add_movie_to_watchlist_by_user_id(user_id: str, movie_id: int):
    movie = await repo.get_movie_by_id(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    updated = await repo.add_movie_id_to_user_watchlist(user_id, movie_id)
    if not updated:
        raise HTTPException(status_code=400, detail="Movie already in watchlist")

    return {"message": f'"{movie["title"]}" added to watchlist'}


async def get_watchlist_by_user_id(user_id: str):
    user = await repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    movie_ids = user.get("movies_watchlist", [])
    if not movie_ids:
        return {"watchlist": []}

    movies = await repo.get_movies_by_ids(movie_ids)
    return {"watchlist": movies}


async def remove_movie_from_watchlist_by_user_id(user_id: str, movie_id: int):
    updated = await repo.remove_movie_id_from_user_watchlist(user_id, movie_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found in watchlist")

    return {"message": f"Movie with id {movie_id} removed from watchlist"}
