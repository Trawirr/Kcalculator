# Generated by Django 4.2.5 on 2023-11-23 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0003_drink_food_delete_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='cup_factor',
        ),
    ]