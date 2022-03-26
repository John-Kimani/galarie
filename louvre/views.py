from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    '''
    View function for louvre app
    '''
    return HttpResponse('Hello louvre!')
