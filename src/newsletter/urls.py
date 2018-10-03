from . import views
from django.urls import path

from newsletter.views import newsletterSubscribe

app_name = 'newsletter'
urlpatterns = [
    path('newsletter/', newsletterSubscribe),
]