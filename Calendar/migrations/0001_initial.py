# Generated by Django 4.2.5 on 2024-02-08 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Calculator', '0014_remove_meal_calendar_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('recipeingredient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Calculator.recipeingredient')),
                ('meal_type', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('d', 'Dessert'), ('S', 'Snack'), ('O', 'Other')], default='O', max_length=1)),
                ('calendar_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='Calendar.calendarday')),
            ],
            bases=('Calculator.recipeingredient',),
        ),
    ]
