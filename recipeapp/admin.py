from django.contrib import admin
from .models import Chef,Recipe,foods

class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal =('food',)

# Register your models here.
admin.site.register(Chef)
admin.site.register(Recipe)
admin.site.register(foods)
