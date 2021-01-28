from django.db import models

# Create your models here.
class Chef(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class food(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class recipe(models.Model):
    name = models.CharField(max_length =60)
    ingredients = models.TextField()
    procedure = models.TextField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    food=models.ManyToManyField(food)
    pub_date = models.DateTimeField(auto_now_add=True)
    
