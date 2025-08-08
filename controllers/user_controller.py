# controllers/user_controller.py
from fastapi import APIRouter
from models.user_model import UserCreate, UserLogin
import services.user_service as service
from typing import List

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", response_model=str, status_code=201)
async def register(user: UserCreate):
    return await service.register_user(user)

@router.post("/login")
async def login(credentials: UserLogin):
    return await service.login_user(credentials)

# ➕ Add to watchlist
@router.post("/{user_id}/watchlist/{movie_id}")
async def add_to_watchlist(user_id: str, movie_id: int):
    return await service.add_to_watchlist(user_id, movie_id)

# 📜 Get watchlist
@router.get("/{user_id}/watchlist")
async def get_watchlist(user_id: str):
    return await service.get_watchlist(user_id)

# ❌ Remove from watchlist
@router.delete("/{user_id}/watchlist/{movie_id}")
async def remove_from_watchlist(user_id: str, movie_id: int):
    return await service.remove_from_watchlist(user_id, movie_id)
