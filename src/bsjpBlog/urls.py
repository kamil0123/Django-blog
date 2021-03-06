"""bsjpBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('posts.urls', namespace='posts')),
    path('', include('contactMessage.urls', namespace='message')),
    path('', include('newsletter.urls', namespace='newsletter')),
    path('', include('places.urls', namespace='places')),

    path('o-mnie/', TemplateView.as_view(template_name='aboutMePage.html'), name='aboutMe'),
    path('kontakt/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('oferta/', TemplateView.as_view(template_name='offer.html'), name='offer'),
    path('cookies/', TemplateView.as_view(template_name='cookies.html'), name='cookies'),
    
    path('potwierdzenie-zapisu/', TemplateView.as_view(template_name='newsletterConfirm.html'), name='newslettterConfirm'),
    path('newsletter-dziekuje/', TemplateView.as_view(template_name='newsletterConfirmed.html'), name='newslettterConfirmed'),
    
    path('obliczanie-predkosci-biegu/', TemplateView.as_view(template_name='speedCalculation.html'), name='speedCalculation'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
