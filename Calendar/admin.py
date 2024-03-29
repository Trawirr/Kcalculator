from django.contrib import admin
from .models import *

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_type', 'calendar_day_desc')

    ordering = ('calendar_day', )

    def calendar_day_desc(self, obj):
        calendar_day = obj.calendar_day
        return f'{calendar_day.date} {calendar_day.user.username}'
    
class MealInLine(admin.TabularInline):
    model = Meal

@admin.register(CalendarDay)
class CalendarDayAdmin(admin.ModelAdmin):
    inlines = [
        MealInLine
    ]
    list_display = ('user', 'date')

    ordering = ('user', )


