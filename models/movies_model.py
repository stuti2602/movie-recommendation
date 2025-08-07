from pydantic import BaseModel
from typing import Optional, List

class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: List[str]
    rating: float
