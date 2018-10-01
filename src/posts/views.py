from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

# Create your views here.

class PostsView(View):
  def get(self, request, *args, **kwargs):

    today = timezone.now().date()
    page_request_var = "page"
    
    queryset_list = Post.objects.active() #.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
      queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
      queryset_list = queryset_list.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(user__first_name__icontains=query) |
        Q(user__last_name__icontains=query)
        ).distinct()

    query = request.GET.get("category")
    if query:
      queryset_list = queryset_list.filter(
        Q(category__name__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 20) # Show n contacts per page
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
        "page_request_var": page_request_var,
        "today": today
    }
    return render(request, "index.html", context)

class PostView(View):
  def get(self, request, slug=None, *args, **kwargs):
    instance = get_object_or_404(Post, slug=slug)

    if instance.publish > timezone.now().date() or instance.draft:
      if not request.user.is_staff or not request.user.is_superuser:
        raise Http404


    
    context = {
      "title": instance.title,
      "instance": instance,
    }
    return render(request, "post.html", context)

