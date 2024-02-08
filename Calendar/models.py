from django.db import models
from Calculator.models import *
from django.contrib.auth.models import User

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