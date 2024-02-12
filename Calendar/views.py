from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date, timedelta
from .models import *

def main_view(request):
    today = date.today()
    monday = today - timedelta(days=today.isoweekday()-1)
    monday.strftime("%d.%m.%y")
    dates = [monday + timedelta(days=i) for i in range(7)]
    calendar_days = [CalendarDay.objects.get(user=request.user, date=d) if CalendarDay.objects.filter(user=request.user, date=d).exists() else None for d in dates]

    context = {
        'today': today,
        'dates': dates,
        'calendar_days': calendar_days,
        'meal_types': Meal.MEAL_CHOICES,
        'meal_icons': {
            'B': 'breakfast_dining',
            'L': 'lunch_dining',
            'D': 'dinner_dining',
            'd': 'bakery_dining',
            'S': "local_pizza",
            'O': 'local_dining'
        }
    }
    return render(request, 'calendar_templates/calendar.html', context)