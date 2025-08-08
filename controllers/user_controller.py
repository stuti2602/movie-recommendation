# controllers/user_controller.py
from fastapi import APIRouter, Header
from models.user_model import UserCreate, UserLogin
from pydantic import BaseModel
import services.user_service as user_service
import services.watchlist_service as watchlist_service

router = APIRouter(prefix="/user", tags=["User"])

class AddWatchlistRequest(BaseModel):
    movie_title: str  # Now title instead of ID

@router.post("/register", response_model=str, status_code=201)
async def register(user: UserCreate):
    return await user_service.register_user(user)

@router.post("/login")
async def login(credentials: UserLogin):
    return await user_service.login_user(credentials)


@router.post("/watchlist", status_code=201)
async def add_to_watchlist(request: AddWatchlistRequest, x_user_email: str = Header(...)):
    return await watchlist_service.add_movie_to_watchlist_by_email(x_user_email, request.movie_title)

@router.get("/watchlist")
async def get_watchlist(x_user_email: str = Header(...)):
    return await watchlist_service.get_watchlist_by_email(x_user_email)


@router.delete("/watchlist", status_code=200)
async def remove_from_watchlist(
    x_user_email: str = Header(...),
    x_movie_title: str = Header(...)
):
    return await watchlist_service.remove_movie_from_watchlist_by_email(x_user_email, x_movie_title)
