from django.shortcuts import render
from .models import Location, Image
# Create your views here.

def index(request):
    '''
    View function for louvre app
    '''
    images = Image.objects.all()
    location = Location.find_location()

    return render(request, 'louvre/index.html', {'images':images}, {'locations':location})

def find_image_location(request, location):
    '''
    View function on modal display
    '''
    images = Image.objects.filter(location_name=location)

    return render(request, 'louvre/location.html', {'location_images': images})
