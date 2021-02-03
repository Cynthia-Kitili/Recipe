from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

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
    chef = models.ForeignKey(User, on_delete=models.CASCADE, default='1', blank = True)
    # food=models.ManyToManyField(foods)
    post = HTMLField( default='1')
    pub_date = models.DateTimeField(auto_now_add=True)
    food_image = models.ImageField(upload_to = 'recipe/',  default='1', blank = True)

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

class RecipeMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

class Location(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations
    
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(blank=True, null=True,upload_to='images/')
    name = models.CharField(max_length=60)
    # author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    # description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image = CloudinaryField('images', default='media/default.jpg')
    # image= models.ImageField(upload_to = 'images/')
    food_name = models.CharField(max_length =60, default='1')
    ingredients = models.TextField(default='1')
    procedure = models.TextField(default='1')
    chef = models.ForeignKey(User, on_delete=models.CASCADE, default='1', blank = True)
    # food=models.ManyToManyField(foods)
    post = HTMLField( default='1')
    # pub_date = models.DateTimeField(auto_now_add=True,default='1')
    # food_image = models.ImageField(upload_to = 'recipe/',  default='1', blank = True)
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    
    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['name']