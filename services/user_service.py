# services/user_service.py
from passlib.context import CryptContext
from models.user_model import UserCreate, UserLogin
import repositories.user_repository as repo
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

async def register_user(user: UserCreate):
    if await repo.find_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already exists")

    user_dict = user.dict()
    user_dict["password_hash"] = hash_password(user_dict.pop("password"))
    user_dict["movies_watchlist"] = []

    return await repo.insert_user(user_dict)

async def login_user(credentials: UserLogin):
    user = await repo.find_by_email(credentials.email)
    if not user or not verify_password(credentials.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "preferences": user["preferences"]
    }

# ➕ Add to watchlist
async def add_to_watchlist(user_id: str, movie_id: int):
    user = await repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    movie_exists = await repo.movies_collection.find_one({"_id": movie_id})
    if not movie_exists:
        raise HTTPException(status_code=404, detail="Movie not found")

    await repo.add_movie_to_watchlist(user_id, movie_id)
    return {"message": "Movie added to watchlist"}

# 📜 Get watchlist
async def get_watchlist(user_id: str):
    movies = await repo.get_watchlist_movies(user_id)
    if movies is None:
        raise HTTPException(status_code=404, detail="User not found")
    return movies

# ❌ Remove from watchlist
async def remove_from_watchlist(user_id: str, movie_id: int):
    user = await repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await repo.remove_movie_from_watchlist(user_id, movie_id)
    return {"message": "Movie removed from watchlist"}
