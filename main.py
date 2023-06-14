from fastapi import FastAPI
from routes.food_routes import food_Router
# import requests
# from pydantic import BaseModel 

app = FastAPI()

app.include_router(food_Router)

@app.get("/")
def read_root():
    return  "Hello Welcome to my website"
