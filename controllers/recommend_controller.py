from fastapi import APIRouter, Header
from typing import List
from models.movies_model import Movie
import services.recommend_service as service

router = APIRouter(tags=["Recommend"])

@router.get("/recommend", response_model=List[Movie])
async def recommend_movies(x_user_id: str = Header(...)):
    return await service.get_recommendations(x_user_id)

