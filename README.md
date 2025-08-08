🎬 Movie Recommendation System — FastAPI + MongoDB
This is a simple Movie Recommendation System built using FastAPI and MongoDB, allowing users to register, store preferences, and receive movie recommendations based on their interests.

📁 Project Structure
movie-recommendation/
│
├── config/                     # MongoDB connection config
│   └── (files for DB setup)
│
├── controllers/               # (Removed)
│
├── data/                      # Data files or scripts
│   └── (if any)
│
├── models/                    # Pydantic models or DB schemas
│   └── (user, movie models, etc.)
│
├── repositories/              # Logic to interact with the database
│   └── (user, movie repositories)
│
├── seed/                      # Seeding scripts for movies
│   └── (movies seeding script)
│
├── services/                  # Business logic
│   └── (user signup/signin logic)
│
├── main.py                    # FastAPI app entry point
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation

🧠 Data Structure (MongoDB Collections)
🧍
{
  "id": ObjectId,
  "name": "John Doe",
  "email": "john@example.com",
  "password_hash": "hashed_password",
  "preferences": ["Action", "Comedy"]
}
🎥 MOVIES

{
  "id": ObjectId,
  "title": "Inception",
  "genre": "Sci-Fi",
  "director": "Christopher Nolan",
  "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"]
}
⭐ USER_WATCHLIST

{
  "id": ObjectId,
  "user_id": ObjectId,
  "movie_id": ObjectId
}
⚙️ How to Run Locally
✅ Step 1: Clone the Repository

git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation
✅ Step 2: Set Up Python Environment
Make sure Python 3.9+ is installed.

Create a virtual environment:


python -m venv venv
source venv/bin/activate     # On Windows use: venv\Scripts\activate
✅ Step 3: Install Dependencies

pip install -r requirements.txt

✅ Step 4: Configure MongoDB
Ensure you have MongoDB installed and running locally, or use MongoDB Atlas.

Create a .env file in your project root:

python -m venv .venv

//in order to check the virtual environment activation use these commands-

.venv\Scripts\activate (Windows)
.venv/Scripts/activate (Bash)


MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=movieDB
🔐 Replace the URI with your connection string if using MongoDB Atlas.

✅ Step 5:🧪 Movie Seeding Script (seed_movies.py)
This script reads a CSV file (data/movies.csv) containing movie details and inserts them into the MongoDB collection (movies_collection). It prevents duplicate seeding by checking if movies are already present in the collection.

✅ What It Does:
Checks if the movie database already contains entries.

Reads movie data from a CSV file.

Parses each movie’s details: id, title, description, genre, and rating.

Splits the genre string into a list for better filtering and querying.

Bulk inserts all movies into the MongoDB collection using insert_many.

📌 Location of the CSV:

data/movies.csv

🏁 How to Run the Script:
Ensure MongoDB is running and your connection is properly configured in config/db.py, then run:

python -m seed.seed_movies

This will populate your MongoDB with movie data if it's currently empty.


✅ Step 6: Run the Server

uvicorn main:app --reload
Server will start at:
👉 http://127.0.0.1:8000
Interactive API docs available at:
👉 http://127.0.0.1:8000/docs





📮 API Endpoints
Endpoint	Method	Description
/users/	POST	Register a new user
/users/login	POST	User login
/movies/	POST	Add new movie
/movies/recommend/{user_id}	GET	Recommend movies based on user preferences
/watchlist/add	POST	Add movie to user watchlist
/watchlist/{user_id}	GET	View user watchlist

🔐 Features
User registration and login with hashed passwords

Movie CRUD operations

Watchlist management

Recommendations based on user genre preferences

MongoDB for persistent storage

FastAPI Swagger UI for easy testing

👩‍🏫 For Reviewers
To run and test this application:

Ensure MongoDB is running locally or provide an Atlas URI.

Run uvicorn as shown above.

Visit /docs to interact with the full API without writing external clients.

Data is stored in the MongoDB collections: users, movies, and watchlists.


