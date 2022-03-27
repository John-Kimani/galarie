from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'), #path to my domain.com/louvre
    path('', views.gallery, name='gallery'),
    path('search/', views.search, name='search')
]