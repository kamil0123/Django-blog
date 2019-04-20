from . import views
from django.urls import path
from places.views import PlaceView, PlacesView, PlacesList

app_name = 'places'
urlpatterns = [
    path('miejsca-przyjazne-dzieciom/', PlacesList.as_view(), name='places'),
    path('miejsce/<slug:slug>/', PlaceView.as_view(), name='place'),
]