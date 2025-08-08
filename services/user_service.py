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
