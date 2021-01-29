from django.test import TestCase
from .models import Chef,Recipe,food


# Create your tests here.
class ChefTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.cynthia= Chef(first_name = 'Cynthia', last_name ='Kitili', email ='kitili@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cynthia,Chef))
    
    # Testing Save Method
    def test_save_method(self):
        self.cynthia.save_chef()
        chefs = Chef.objects.all()
        self.assertTrue(len(chefs) > 0)

class RecipeTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.cynthia= Chef(first_name = 'Cynthia', last_name ='Kitili', email ='kitili@moringaschool.com')
        self.cynthia.save_chef()

        # Creating a new tag and saving it
        self.new_food = foods(name = 'testing')
        self.new_food.save()

        self.new_recipe= Recipe(chef =self.cynthia ,food_name = ' chicken',ingredients = 'water, salt' procedure= "boil chicken")
        self.new_recipe.save()

        self.new_recipe.foods.add(self.new_food)

    def tearDown(self):
        Chef.objects.all().delete()
        foods.objects.all().delete()
        Recipe.objects.all().delete()

