# Generated by Django 3.1.6 on 2021-02-01 17:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0003_remove_recipe_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='post',
            field=tinymce.models.HTMLField(default='None '),
        ),
    ]
