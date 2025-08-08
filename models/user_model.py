from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    preferences: List[str] = Field(..., min_items=1, max_items=3)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    preferences: List[str]
    watchlist: List[str] = []
