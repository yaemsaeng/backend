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

@food_Router.get("/search/{Title}", tags=["reccomend food"])
async def get_similar_foods(Title: str):
    regex = re.compile(f".*{Title}.*", re.IGNORECASE)
    similar_foods = foods_serializer(collection.find({"Title": regex}))
    image_names = [food["Image_Name"] + ".jpg" for food in similar_foods]

    urls = []
    for image_name in image_names:
        blob = bucket.blob(image_name)
        url = blob.generate_signed_url(
            expiration=datetime.timedelta(days=7),
        )
        urls.append(url)

    # เปลี่ยนค่า "Image_Name" ใน similar_foods เป็นค่าจาก urls
    for i, food in enumerate(similar_foods):
        food["Image_Name"] = urls[i]

    return similar_foods
    
