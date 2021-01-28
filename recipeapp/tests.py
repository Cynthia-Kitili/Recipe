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
