from django.contrib import admin
from .models import Post, Category

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
  list_display = ["title", "updated", "created"]
  list_display_links = ["updated"]
  list_editable = ["title"]
  list_filter = ["created", "updated"]
  search_fields = ["title", "content"]
  
  class Meta:
    model = Post

class CategoryModelAdmin(admin.ModelAdmin):
  list_display = ["name"]
  list_display_links = ["name"]

  class Meta:
    model = Category

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)

