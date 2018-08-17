from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

class PostsView(View):
  def get(self, request, *args, **kwargs):
    page_request_var = "page"
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
    page = request.GET.get(page_request_var)

    try:
      queryset = paginator.page(page)
    except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      queryset = paginator.page(1)
    except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list" : queryset,
        "title": "List",
        "page_request_var": page_request_var
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

