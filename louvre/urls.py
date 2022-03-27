from django.urls import path
from . import views

urlpatterns = [
    path('louvre/', views.index, name='gallery') #path to my domain.com/louvre
]