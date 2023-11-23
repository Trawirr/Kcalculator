from django.shortcuts import render

def main_view(request):
    print("Main view")
    context = {}
    return render(request, 'calculator_templates/calculator.html', context)

def add_ingredient(request):
    print("Add ingredient")
    context = {}
    return render(request, 'calculator_templates/add_ingredient.html', context)

def calculate(request):
    print(f"Calculate, get: {request.GET}")
    context = {}
    return render(request, 'calculator_templates/add_ingredient.html', context)