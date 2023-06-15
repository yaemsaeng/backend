import datetime
from fastapi import APIRouter
# from model.food_model import Food,Name_Food
from schemas.food_schema import foods_serializer
# from bson import ObjectId
from config.db import collection
import firebase_admin
from firebase_admin import credentials, storage
import re

food_Router = APIRouter()

cred = credentials.Certificate("./firebase/food-5fd0f-firebase-adminsdk-j0le2-69726e360d.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'food-5fd0f.appspot.com'})
bucket = storage.bucket()

@food_Router.get("/image_url/{image_name}", tags=["food"])
def get_image_url(image_name: str):
    blob = bucket.blob(image_name)
    url = blob.generate_signed_url(
        expiration=datetime.timedelta(days=7),  # ตั้งค่าเวลาหมดอายุของ URL
    )
    return url

@food_Router.get("/search/{Title}" , tags=["search food"]) 
async def get_similar_foods(Title: str):
    regex = re.compile(f".*{Title}.*", re.IGNORECASE)
    similar_foods = foods_serializer(collection.find({"Title": regex}))
    return similar_foods

@food_Router.get("/reccomend/{Title}", tags=["reccomend food"])
async def get_similar_foods(Title: str):
    regex = re.compile(f".*{Title}.*", re.IGNORECASE)
    similar_foods = collection.find({"Title": regex})
    formatted_foods = [{"Title": food["Title"], "Ingredients": food["Ingredients"]} for food in similar_foods]
    return formatted_foods
