from django.db import models

# import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.

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