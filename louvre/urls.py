from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('index', views.index, name='index'), #path to my domain.com/louvre
    path('', views.gallery, name='gallery'),
    path('search/', views.search, name='search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)