# Generated by Django 3.1.5 on 2021-01-29 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0005_auto_20210129_2120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='food',
            new_name='foods',
        ),
    ]