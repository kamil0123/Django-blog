from . import views
from django.urls import path
from posts.views import PostView, PostsView

app_name = 'posts'
urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
    path('post/<slug:slug>/', PostView.as_view(), name='post'),
]