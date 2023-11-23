from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "protein", "carbs", "fat")
    ordering = ("name", )