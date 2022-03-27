from django.db import models

# import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.
class Category(models.Model):
    '''
    class that handles image category
    '''
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    '''
    Class that handles Images
    '''
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=30, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    @classmethod
    def find_by_location(cls, location):
        '''
        Function to filter image using location
        '''
        image_location = Image.objects.filter(location_name=location)

        return image_location

    @classmethod
    def image_update(cls, id, value):
        '''
        Function to enable admin update images
        '''
        image = cls.objects.filter(id=id).update(image=value)
        return image

    @classmethod
    def find_image_by_category(cls, category):
        '''
        Function that filters images using category
        '''
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name


class Location(models.Model):
    '''
    class that handles location instances
    '''
    name = models.CharField(max_length=40, unique=True)

    @classmethod
    def find_location(cls):
        '''
        Function that enable to get location
        '''
        location = Location.objects.all()
        
        return location
