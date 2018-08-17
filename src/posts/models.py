from django.db import models
from django.urls import reverse

# Create your models here.

def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
  title = models.CharField(max_length=160)
  content = models.TextField()
  image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
  height_field = models.IntegerField(default=0)
  width_field = models.IntegerField(default=0)
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  created = models.DateTimeField(auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("posts:post", kwargs={"id": self.id}) 

  class Meta:
  	ordering = ["-created", "-updated"]