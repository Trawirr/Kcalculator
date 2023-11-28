from django.contrib import admin
from .models import *

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "protein", "carbs", "fat", "kcal")
    ordering = ("name", "kcal")
    
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", )
    ordering = ("name", )