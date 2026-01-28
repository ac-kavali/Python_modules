def validate_ingredients (ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]

    # split the input string by spaces to get each ingredient
    ingredient_list = ingredients.split()

    # check if every ingredient is in the valid list
    if all(item in valid_ingredients for item in ingredient_list):
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
