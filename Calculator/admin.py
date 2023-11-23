from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "protein", "carbs", "fat", "kcal", "piece_factor")
    ordering = ("name", "kcal")
    
@admin.register(Drink)
class Drink(admin.ModelAdmin):
    list_display = ("name", "protein", "carbs", "fat", "kcal", "cup_factor")
    ordering = ("name", "kcal")