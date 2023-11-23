from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('add-ingredient', views.add_ingredient, name='add-ingredient'),
    path('calculate', views.calculate, name='calculate'),
]