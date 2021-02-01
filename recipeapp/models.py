from django.db import models
import datetime as dt

# Create your models here.
class Chef(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.first_name

    def save_chef(self):
        self.save()    

class foods(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    food_name = models.CharField(max_length =60)
    ingredients = models.TextField()
    procedure = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    food=models.ManyToManyField(foods)
    pub_date = models.DateTimeField(auto_now_add=True)
    food_image = models.ImageField(upload_to = 'recipe/', default="DEFAULT VALUE")

    @classmethod
    def todays_recipe(cls):
        today = dt.date.today()
        recipe = cls.objects.filter(pub_date__date = today)
        return recipe

    @classmethod
    def days_recipe(cls,date):
        recipe = cls.objects.filter(pub_date__date = date)
        return recipe
    
    @classmethod
    def search_by_food_name(cls,search_term):
        recipe = cls.objects.filter(food_name__icontains=search_term)
        return recipe

class RecipeRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

