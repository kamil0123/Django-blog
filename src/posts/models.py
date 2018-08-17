from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=160)
  content = models.TextField()
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  created = models.DateTimeField(auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("posts:post", kwargs={"id": self.id}) 

  class Meta:
  	ordering = ["-created", "-updated"]