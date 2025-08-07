from fastapi import FastAPI
from routes.movie_routes import router as movie_router

app = FastAPI()

app.include_router(movie_router, prefix="/movies", tags=["Movies"])

@app.get("/")
def read_root():
    return {"message": "Movie Recommendation API"}