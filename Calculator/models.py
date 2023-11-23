from django.db import models

# Create your models here.
class Ingredient(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50, default="New ingredient")
    protein = models.FloatField(default=0, verbose_name="protein/100g_ml")
    carbs = models.FloatField(default=0, verbose_name="carbs/100g_ml")
    fat = models.FloatField(default=0, verbose_name="fat/100g_ml")
    kcal = models.FloatField(default=0, verbose_name="kcal/100g_ml")

class Food(Ingredient):
    piece_factor = models.IntegerField(default=0, verbose_name="Avg piece weight")

class Drink(Ingredient):
    pass

    # --ADD-- methods for spoons, cups etc.