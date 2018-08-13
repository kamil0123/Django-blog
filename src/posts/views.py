from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

class PostsView(View):
  def get(self, request, *args, **kwargs):
    queryset = Post.objects.all()
    context = {
      "object_list" : queryset
    }
    return render(request, "index.html", context)

class PostView(View):
  def get(self, request, id=None, *args, **kwargs):
    instance = get_object_or_404(Post, id=id)
    context = {
      "title": instance.title,
      "instance": instance,
    }
    return render(request, "post.html", context)

