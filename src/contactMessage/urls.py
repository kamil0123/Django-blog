from . import views
from django.urls import path

from contactMessage.views import contactView


app_name = 'contactMessage'
urlpatterns = [
    path('kontakt/', contactView),
]