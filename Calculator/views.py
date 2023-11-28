from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .utils.utils import get_ingredient
from django.views.decorators.csrf import csrf_exempt

def main_view(request):
    print("Main view")
    context = {
        "ingredients": [i for i in Ingredient.objects.all().values_list("name", flat=True)] # [f for f in Food.objects.all().values_list("name", flat=True)] + [d for d in Drink.objects.all().values_list("name", flat=True)]
    }
    print(context)
    return render(request, 'calculator_templates/calculator.html', context)

def add_ingredient(request):
    print("Add ingredient")
    context = {}
    return render(request, 'calculator_templates/add_ingredient.html', context)

def calculate(request):
    values = {
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "kcal": 0,
    }

    volumes = [int(v) for v in request.GET.getlist('volumes[]')]
    units = [u for u in request.GET.getlist('units[]')]
    for i, ingredient in enumerate(request.GET.getlist("ingredients[]")):
        print(ingredient, volumes[i], units[i])
        ingredient_object = get_ingredient(ingredient)
        print(ingredient_object.get_macro(volumes[i], units[i]))
        for k, v in ingredient_object.get_macro(volumes[i], units[i]).items():
            values[k] += v

    return HttpResponse(f"<p>Kcal: {values['kcal']:.2f}, protein: {values['protein']:.2f}, carbs: {values['carbs']:.2f}, fat: {values['fat']:.2f}</p>")

def recipes_view(request):
    print("Recipes view")
    context = {
        "ingredients": [i for i in Ingredient.objects.all().values_list("name", flat=True)] #[f for f in Food.objects.all().values_list("name", flat=True)] + [d for d in Drink.objects.all().values_list("name", flat=True)]
    }
    print(context)
    return render(request, 'calculator_templates/recipes.html', context)

def add_recipe(request):
    pass

def get_units(request):
    ingredient_name = request.GET.get("ingredients[]", "")
    print(ingredient_name)
    try:
        ingredient = get_ingredient(ingredient_name)
        print(ingredient)
        return HttpResponse(f"""<input class="unit-input" type="text" name="units[]" placeholder="{', '.join(ingredient.get_units())}">""")
    except Exception as e:
        print(e)
        return HttpResponse("""<input class="unit-input" type="text" name="units[]" placeholder="unit">""")
    
@csrf_exempt
def delete_row(request):
    return HttpResponse('')