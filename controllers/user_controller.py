from fastapi import APIRouter
from models.user_model import UserCreate, UserLogin, UserOut
import services.user_service as service

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", response_model=str, status_code=201)
async def register(user: UserCreate):
    return await service.register_user(user)

@router.post("/login")
async def login(credentials: UserLogin):
    return await service.login_user(credentials)
