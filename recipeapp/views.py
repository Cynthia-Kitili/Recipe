from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def recipe_of_day(request):
    date = dt.date.today()
    return render(request, 'all-recipes/today-recipe.html', {"date": date,})   

def past_days_recipe(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(recipe_of_day)

    return render(request, 'all-recipes/past-recipe.html', {"date": date})

