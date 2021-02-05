from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.recipe_today,name='recipeToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_recipe,name = 'pastRecipe'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^recipe/(\d+)',views.recipe, name ='recipe'),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'^new/image$', views.new_recipe, name='new-recipe'),
    url(r'^ajax/recipeletter/$', views.recipeletter, name='recipeletter'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',views.MerchDescription.as_view()),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^accounts/profile/$',views.profile,name='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
