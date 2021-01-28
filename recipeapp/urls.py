from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.recipe_of_day,name='recipeToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_recipe,name = 'pastRecipe')

]
