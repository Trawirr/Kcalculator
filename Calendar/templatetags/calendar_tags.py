from django import template
from Calendar.models import CalendarDay

register = template.Library()

@register.filter(name='count_meals')
def count_meals(calendar_day:CalendarDay, meal_type:str):
    return calendar_day.meals.filter(meal_type=meal_type).count()

@register.simple_tag
def sum_macro(calendar_day:CalendarDay, meal_type:str):
    return calendar_day.sum_macro(meal_type)

@register.simple_tag
def get_icon(icons, meal_type):
    return icons[meal_type]