from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def main_view(request):
    print("Main view")
    context = {"ingredients": Ingredient.objects.all().values_list("name", flat=True)}
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
    for i, ingredient in enumerate(request.GET.getlist("ingredients[]")):
        print(ingredient, volumes[i])
        ingredient_object = Ingredient.objects.get(name = ingredient)
        values['protein'] += ingredient_object.protein * volumes[i] / 100
        values['carbs'] += ingredient_object.carbs * volumes[i] / 100
        values['fat'] += ingredient_object.fat * volumes[i] / 100
        values['kcal'] += ingredient_object.kcal * volumes[i] / 100

    return HttpResponse(f"<p>Kcal: {values['kcal']:.2f}, protein: {values['protein']:.2f}, carbs: {values['carbs']:.2f}, kcal: {values['kcal']:.2f}</p>")