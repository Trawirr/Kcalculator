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

    cup_factor = 250 # ml
    tbsp_factor = 15 # ml
    tsp_factor = 5 # ml

    def get_units(self):
        return []

class Food(Ingredient):
    piece_factor = models.FloatField(default=0, verbose_name="Avg piece weight")
    ml_factor = models.FloatField(default=0, verbose_name="ml/100g")

    def get_units(self):
        units = ['g']
        if self.piece_factor > 0: units.append('pc')
        if self.ml_factor > 0: units += ['ml', 'tbsp', 'tsp']
        return units

class Drink(Ingredient):
    
    def get_units(self):
        return ['ml', 'cup', 'tbsp', 'tsp']

    # --ADD-- methods for spoons, cups etc.