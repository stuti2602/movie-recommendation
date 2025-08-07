from fastapi import FastAPI
from controllers import user_controller,recommend_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(recommend_controller.router)

@app.get("/")
def read_root():
    return {"message": "Movie Recommendation API"}
