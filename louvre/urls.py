from django.urls import path
from . import views

urlpatterns = [
    path('louvre/', views.index) #path to my domain.com/louvre
]