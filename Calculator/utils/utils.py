from Calculator.models import *
from typing import Union

def get_ingredient(name: str) -> Ingredient:
    if Ingredient.objects.filter(name=name).exists():
        return Ingredient.objects.get(name=name)
    else:
        raise Exception("IngredientNotFound")