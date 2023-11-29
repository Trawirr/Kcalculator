from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50, default="New ingredient")
    protein = models.FloatField(default=0, verbose_name="protein/100g_ml")
    carbs = models.FloatField(default=0, verbose_name="carbs/100g_ml")
    fat = models.FloatField(default=0, verbose_name="fat/100g_ml")
    kcal = models.FloatField(default=0, verbose_name="kcal/100g_ml")

    default_unit = models.CharField(max_length=2, default='g')
    ml_factor = models.FloatField(default=0, verbose_name="ml/100g")
    piece_factor = models.FloatField(default=0, verbose_name="Avg piece weight")

    cup_factor = 250 # ml
    tbsp_factor = 15 # ml
    tsp_factor = 5 # ml
    
    def __str__(self) -> str:
        return self.name

    def get_units(self) -> list:
        units = [self.default_unit]
        if self.piece_factor > 0: units.append('pc')
        if self.ml_factor > 0 or self.default_unit == 'ml': units += ['ml', 'cup', 'tbsp', 'tsp']
        return units
    
    def get_macro(self, volume: int, unit: str) -> dict:
        if unit in self.get_units():
            values = {
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "kcal": 0,
            }

            # grams
            if self.default_unit == 'g':
                if unit == 'pc':
                    volume *= self.piece_factor
                elif unit not in ['g', 'pc'] and self.ml_factor > 0:
                    volume /= self.ml_factor
                    if unit != 'ml':
                        volume *= getattr(self, f"{unit}_factor")
            else:
                if unit != 'ml':
                    volume *= getattr(self, f"{unit}_factor")
            
            values['protein'] += self.protein * volume / 100
            values['carbs'] += self.carbs * volume / 100
            values['fat'] += self.fat * volume / 100
            values['kcal'] += self.kcal * volume / 100
        return values
    
class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    volume = models.IntegerField(default=0)
    unit = models.CharField(max_length=4, default='g')

    def __str__(self) -> str:
        return f"{self.ingredient.name} {self.volume}{self.unit}"
    
    def get_macro(self) -> dict:
        return self.ingredient.get_macro(self.volume, self.unit)

class Recipe(models.Model):
    name = models.CharField(max_length=60, unique=True)
    ingredients = models.ManyToManyField(RecipeIngredient, related_name="recipes")
    piece_factor = models.FloatField(default=0, verbose_name="Avg piece weight")

    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_volume(self):
        volume = 0
        for ingredient in self.ingredients:
            volume += ingredient.volume
        return volume
    
    def get_macro(self) -> dict:
        values = {
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "kcal": 0,
            }
        
        for ingredient in self.ingredients:
            for k, v in ingredient.ingredient.get_macro().items():
                values[k] += v
        return values * 100 / self.get_volume()