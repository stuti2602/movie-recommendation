from config.db import db
from bson import ObjectId

users_collection = db.get_collection("users")

async def find_by_email(email: str):
    return await users_collection.find_one({"email": email})

async def insert_user(user_data: dict):
    result = await users_collection.insert_one(user_data)
    return str(result.inserted_id)

async def get_user_by_id(user_id: str):
    return await users_collection.find_one({"_id": ObjectId(user_id)})
