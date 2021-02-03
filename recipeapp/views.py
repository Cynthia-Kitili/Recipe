from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Recipe, RecipeRecipients
from .forms import RecipeForm, SignUpForm, NewRecipeForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  RecipeMerch
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url="/accounts/login/")
def recipe_today(request):
    images = Image.objects.all()
    locations = Location.objects.all()
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
    


    return render(request, 'all-recipes/today-recipe.html', {"date": date,'images': images[::-1], 'locations':locations,"recipe":recipe,"letterForm":form})   

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

@login_required(login_url='/accounts/login/')
def new_recipe(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.chef = current_user
            image.save()
        return redirect('recipeToday')

    else:
        form = NewRecipeForm()
    return render(request, 'new_recipe.html', {"form": form})

def recipeletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = RecipeRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = RecipeMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
        permission_classes = (IsAdminOrReadOnly,)

class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return RecipeMerch.objects.get(pk=pk)
        except RecipeMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @login_required(login_url='/accounts/login/')
# def photos(request):
    
#     images = Image.objects.all()
#     locations = Location.objects.all()
#     return render(request, 'all-recipes/today-recipe.html',{'images': images[::-1], 'locations':locations})        
         
@login_required(login_url='/accounts/login/')
def location_filter(request, image_location):
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} recipe-today'
    return render(request, 'all-recipes/location.html', {'title':title,'images':images,'location':location})
    
@login_required(login_url='/accounts/login/')
def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'all-recipes/location.html', {'location_images': images})         