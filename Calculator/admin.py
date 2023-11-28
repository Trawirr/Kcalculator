from django.contrib import admin
from .models import *

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "protein", "carbs", "fat", "kcal")
    ordering = ("name", "kcal")
    
@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("ingredient", "volume", "unit", "recipe")
    ordering = ("recipes", )

    def recipe(self, obj):
        recipes_related = obj.recipes.all()
        if recipes_related.exists(): return recipes_related[0].name 
        else: return '-'
        return obj.recipes.all()[0].name

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", )
    ordering = ("name", )