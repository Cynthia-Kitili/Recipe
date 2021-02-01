from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Recipe, RecipeRecipients
from .forms import RecipeForm, SignUpForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url="/accounts/login/")
def recipe_today(request):
    date = dt.date.today()
    recipe = Recipe.todays_recipe()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = RecipeRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('recipe_today')
            
    else:
        form = RecipeForm()

    return render(request, 'all-recipes/today-recipe.html', {"date": date,"recipe":recipe,"letterForm":form})   

@login_required(login_url="/accounts/login/")
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

@login_required(login_url="/accounts/login/")
def search_results(request):

    if 'recipe' in request.GET and request.GET["recipe"]:
        search_term = request.GET.get("recipe")
        searched_recipe = Recipe.search_by_food_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-recipes/search.html',{"message":message,"recipe": searched_recipe})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-recipes/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def recipe(request,recipe_id):
    try:
        recipe = Recipe.objects.get(id = recipe_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-recipes/recipe.html", {"recipe":recipe})

@login_required(login_url="/accounts/login/")
def logout_request(request):
    logout(request)
    return redirect('/')    

def signUp(request):    
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['username']
            email = form.cleaned_data['email']
            send=welcome_email(name,email)
            HttpResponseRedirect('pics')
    else:
        form = SignUpForm()
    return render(request,'registration/registration_form.html',{'form':form})