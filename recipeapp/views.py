from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Recipe

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def recipe_today(request):
    date = dt.date.today()
    recipe = Recipe.todays_recipe()

    return render(request, 'all-recipes/today-recipe.html', {"date": date,"recipe":recipe})   

def past_days_recipe(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(recipe_today)
    recipe = Recipe.days_recipe(date)

    return render(request, 'all-recipes/past-recipe.html', {"date": date,"recipe":recipe})

