from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='calculator-main'),
    path('add-ingredient', views.add_ingredient, name='add-ingredient'),
    path('calculate', views.calculate, name='calculate'),
    path('recipes', views.recipes_view, name='recipes'),
    path('add-recipe', views.add_recipe, name='add-recipe'),
    path('get-units', views.get_units, name='get-units'),
    path('delete-row', views.delete_row, name='delete-row'),
]