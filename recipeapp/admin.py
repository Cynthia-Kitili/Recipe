from django.contrib import admin
from .models import Chef,Recipe,foods

class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal =('food',)

# Register your models here.
admin.site.register(Chef)
admin.site.register(Recipe)
admin.site.register(foods)

from .models import Category,Location,Image

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal =('image',)

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)