from unicodedata import category
from django.shortcuts import render
from .models import Location, Image
# Create your views here.

def index(request):
    '''
    View function for louvre app
    '''
    return render(request, 'index.html')

def gallery(request):
    '''
    Test gallery
    '''
    images = Image.objects.all()
    location = Location.find_location()
    my_gallery = {'images':images}

    return render(request, 'gallery.html', my_gallery)

def find_image_location(request, location):
    '''
    View function on modal display
    '''
    images = Image.objects.filter(location_name=location)

    return render(request, 'louvre/location.html', {'location_images': images})

def search(request):
    '''
    View function that enables search
    '''
    if 'imagesearched' in request.GET and request.GET['imagesearched']:
        category = request.GET.get("imagesearched")
        searched_images = Image.find_image_by_category(category)
        message = f"{category}"

        return render(request, 'search.html', {'message': message, 'images':searched_images})
    else:
        message = 'Invalid search image category'
        return render(request, 'search.html', {'message': message})
