from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.recipe_today,name='recipeToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_recipe,name = 'pastRecipe'),
    url(r'^search/', views.search_results, name='search_results')

]
