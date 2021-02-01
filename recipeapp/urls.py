from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.recipe_today,name='recipeToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_recipe,name = 'pastRecipe'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^recipe/(\d+)',views.recipe, name ='recipe'),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'^new/recipe$', views.new_recipe, name='new-recipe')


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
