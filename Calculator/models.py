from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50, default="New ingredient")
    protein = models.FloatField(default = 0, verbose_name="protein/100g")
    carbs = models.FloatField(default = 0, verbose_name="carbs/100g")
    fat = models.FloatField(default = 0, verbose_name="fat/100g")
    kcal = models.FloatField(default = 0, verbose_name="kcal/100g")