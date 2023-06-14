from pydantic import BaseModel 

class Food(BaseModel):
    id:str
    Title:str 
    Ingredients:str
    Instructions:str
    Image_Name:str
    Cleaned_Ingredients:str

