from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: Optional[str]  # Will be MongoDB ObjectId as str later
    title: str
    genre: str
    director: str
    year: int
    rating: float
