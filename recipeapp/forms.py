from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .models import Recipe

class RecipeForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter Email!')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')   

class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['chef', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
