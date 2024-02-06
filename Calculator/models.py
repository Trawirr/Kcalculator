from django.db import models
from django.contrib.auth.models import User

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

    def get_units(self) -> list[str]:
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

class Recipe(models.Model):
    name = models.CharField(max_length=60, unique=True)
    piece_factor = models.FloatField(default=0, verbose_name="Avg piece weight")

    recipe_as_ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_volume(self):
        volume = 0
        for ingredient in self.ingredients.all():
            volume += ingredient.volume
        return volume
    
    def get_units(self) -> list[str]:
        units = ['g']
        if self.piece_factor > 0: units.append('pc')
        return units
    
    def get_macro_per_100g(self) -> dict:
        values = {
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "kcal": 0,
            }
        
        for ingredient in self.ingredients.all():
            for k, v in ingredient.ingredient.get_macro(ingredient.volume, ingredient.unit).items():
                values[k] += v
        for k, v in values.items():
            values[k] = round(values[k] * 100 / self.get_volume(), 2)
        return values

    def get_macro(self, volume, unit) -> dict:
        values = self.get_macro_per_100g()

        if unit == 'pc':
            volume *= self.piece_factor

        values['protein'] += self.protein * volume / 100
        values['carbs'] += self.carbs * volume / 100
        values['fat'] += self.fat * volume / 100
        values['kcal'] += self.kcal * volume / 100
    
class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    volume = models.IntegerField(default=0)
    unit = models.CharField(max_length=4, default='g')
    recipe = models.ForeignKey(Recipe, default=None, blank=True, null=True, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self) -> str:
        return f"{self.ingredient.name} {self.volume}{self.unit}"
    
    def get_macro(self) -> dict:
        return self.ingredient.get_macro(self.volume, self.unit)

class CalendarDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="days")
    date = models.DateField()
    
class Meal(RecipeIngredient):
    MEAL_CHOICES = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('d', 'Dessert'),
        ('S', "Snack"),
        ('O', 'Other'),
    )

    meal_type = models.CharField(max_length=1, default='O', choices=MEAL_CHOICES)
    calendar_day = models.ForeignKey(CalendarDay, on_delete=models.CASCADE, related_name="meals")
