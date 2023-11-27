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

    def get_units(self) -> list:
        return []
    
    def get_macro(self, volume: int, unit: str) -> dict:
        pass

class Food(Ingredient):
    piece_factor = models.FloatField(default=0, verbose_name="Avg piece weight")
    ml_factor = models.FloatField(default=0, verbose_name="ml/100g")

    def get_units(self) -> list:
        units = ['g']
        if self.piece_factor > 0: units.append('pc')
        if self.ml_factor > 0: units += ['ml', 'tbsp', 'tsp']
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
            if unit != 'g':
                volume /= self.ml_factor
                # other ml unit
                if unit != 'ml':
                    volume *= getattr(self, f"{unit}_factor")
            
            values['protein'] += self.protein * volume / 100
            values['carbs'] += self.carbs * volume / 100
            values['fat'] += self.fat * volume / 100
            values['kcal'] += self.kcal * volume / 100
        return values

class Drink(Ingredient):
    
    def get_units(self) -> list:
        return ['ml', 'cup', 'tbsp', 'tsp']
    
    def get_macro(self, volume: int, unit: str) -> dict:
        if unit in self.get_units():
            values = {
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "kcal": 0,
            }

            # other ml unit
            if unit != 'ml':
                volume *= getattr(self, f"{unit}_factor")
            
            values['protein'] += self.protein * volume / 100
            values['carbs'] += self.carbs * volume / 100
            values['fat'] += self.fat * volume / 100
            values['kcal'] += self.kcal * volume / 100
        return values