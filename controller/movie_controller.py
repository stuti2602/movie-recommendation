from fastapi import APIRouter, HTTPException
from models.movie_model import Movie
from typing import List

router = APIRouter()

# Temporary in-memory storage
movies_db: List[Movie] = []

@router.get("/", response_model=List[Movie])
def get_movies():
    return movies_db

@router.get("/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    for movie in movies_db:
        if movie.title.lower() == title.lower():
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@router.post("/", response_model=Movie)
def add_movie(movie: Movie):
    movies_db.append(movie)
    return movie

@router.put("/{title}", response_model=Movie)
def update_movie(title: str, updated_movie: Movie):
    for i, movie in enumerate(movies_db):
        if movie.title.lower() == title.lower():
            movies_db[i] = updated_movie
            return updated_movie
    raise HTTPException(status_code=404, detail="Movie not found")

@router.delete("/{title}")
def delete_movie(title: str):
    for i, movie in enumerate(movies_db):
        if movie.title.lower() == title.lower():
            del movies_db[i]
            return {"message": "Movie deleted"}
    raise HTTPException(status_code=404, detail="Movie not found")
