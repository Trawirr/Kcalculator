# Generated by Django 4.2.5 on 2023-11-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0004_remove_drink_cup_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='piece_factor',
            field=models.FloatField(default=0, verbose_name='Avg piece weight'),
        ),
    ]
