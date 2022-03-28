from django.test import TestCase
from .models import Category, Image, Location

# Create your tests here.

class LocationTestClass(TestCase):
    '''
    Test class that tests location model
    '''

    def setUp(self):
        self.location = Location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()


class CategoryTestClass(TestCase):
    '''
    Test class that tests category model
    '''
    def setUp(self):
        self.category = Category(name='studio')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save_category()
class ImageTestClass(TestCase):
    '''
    Test class that test image model 
    '''
    def setUp(self):
        self.image = Image(name='Photographer', description='At my studio')

    def test_save_method(self):
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        '''
        Test function to check delete instances on each class
        '''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
