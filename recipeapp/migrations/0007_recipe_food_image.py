# Generated by Django 3.1.5 on 2021-01-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0006_auto_20210129_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='food_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='recipe/'),
        ),
    ]