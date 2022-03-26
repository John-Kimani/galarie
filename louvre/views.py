from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    View function for louvre app
    '''
    return render(request, 'louvre/index.html')
