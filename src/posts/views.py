from django.shortcuts import render
from django.views import View

from .models import Post

# Create your views here.
class PostView(View):
  def get(self, request, *args, **kwargs):
    queryset = Post.objects.all()
    context = {
      "object_list" : queryset
    }
    return render(request, "index.html", context)

