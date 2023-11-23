from Calculator.models import *
from typing import Union

def get_ingredient(name: str) -> Union[Food, Drink]:
    if Food.objects.filter(name=name).exists():
        return Food.objects.get(name=name)
    elif Drink.objects.filter(name=name).exists():
        return Drink.objects.get(name=name)
    else:
        raise Exception("IngredientNotFound")