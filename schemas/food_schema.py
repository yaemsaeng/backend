def food_serializer(food) -> dict:
    return {
        # '_id':str(food["_id"]),
        # 'id':food["id"],
        'Title':food["Title"],
        'Ingredients':food["Ingredients"],
        'Instructions':food["Instructions"],
        'Image_Name':food["Image_Name"],
        'Cleaned_Ingredients':food["Cleaned_Ingredients"]
    }

def foods_serializer(foods) -> list:
    return [food_serializer(food) for food in foods]
 