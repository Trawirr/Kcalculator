from django.db import models
from Calculator.models import *
from django.contrib.auth.models import User

class CalendarDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="days")
    date = models.DateField()

    def sum_macro(self, meal_type):
        meals = self.meals.filter(meal_type=meal_type)
        print(f"meals: {meals}")
        macro = {
            "protein": 0,
            "carbs": 0,
            "fat": 0,
            "kcal": 0,
            }
        for meal in meals:
            print(f"get macro: {meal.get_macro()}")
            for k, v in meal.get_macro().items():
                macro[k] += v

        for k, v in macro.items():
            macro[k] = int(v)

        return f"{macro['protein']}P {macro['carbs']}C {macro['fat']}F {macro['kcal']}kcal"
    
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