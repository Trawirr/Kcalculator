from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50, default="New ingredient")
    protein = models.FloatField(default = 0)
    carbs = models.FloatField(default = 0)
    fat = models.FloatField(default = 0)