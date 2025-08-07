import csv
import asyncio
from config.db import movies_collection

CSV_PATH = "data/movies.csv"

async def seed_movies():
    count = await movies_collection.count_documents({})
    if count > 0:
        print("⚠️ Movies already seeded.")
        return

    movies = []
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = {
                "_id": int(row["id"]),
                "title": row["title"],
                "description": row["description"],
                "genre": row["genre"].split("|"),
                "rating": float(row["rating"])
            }
            movies.append(movie)

    result = await movies_collection.insert_many(movies)
    print(f"✅ Inserted {len(result.inserted_ids)} movies into the database.")

if __name__ == "__main__":
    asyncio.run(seed_movies())
