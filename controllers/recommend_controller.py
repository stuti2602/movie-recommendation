from fastapi import APIRouter, Header, HTTPException
from bson import ObjectId
from config.db import db
from models.movies_model import Movie
from typing import List

router = APIRouter()

@router.get("/recommend", response_model=List[Movie])
async def recommend_movies(x_user_id: str = Header(...)):

    # 1. Get user by ID
    user = await db.users.find_one({"_id": ObjectId(x_user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    preferences = user.get("preferences", [])
    if not preferences:
        raise HTTPException(status_code=400, detail="User has no genre preferences")

    # 2. Find movies matching any of the preferred genres, sort by rating
    cursor = db.movies.find({"genre": {"$in": preferences}}).sort("rating", -1).limit(5)
    movies = await cursor.to_list(length=5)

    return movies