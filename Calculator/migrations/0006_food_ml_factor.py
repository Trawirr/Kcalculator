# Generated by Django 4.2.5 on 2023-11-27 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator', '0005_alter_food_piece_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ml_factor',
            field=models.FloatField(default=0, verbose_name='ml/100g'),
        ),
    ]
