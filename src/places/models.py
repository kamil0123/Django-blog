from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class PlaceQuerySet(models.query.QuerySet):
  def not_draft(self):
    return self.filter(draft=False)
  
  def published(self):
    return self.filter(publish__lte=timezone.now()).not_draft()


class PlaceManager(models.Manager):
  def get_queryset(self, *args, **kwargs):
    return PlaceQuerySet(self.model, using=self._db)

  def active(self, *args, **kwargs):
    return self.get_queryset().published()


def uploadLocation_placeImage(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)

def uploadLocation_categoryImage(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)

class Category(models.Model):
  name = models.CharField(max_length=30)
  image = models.ImageField(upload_to=uploadLocation_categoryImage, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
  height_field = models.IntegerField(default=150)
  width_field = models.IntegerField(default=450) 

  def __str__(self):
    return self.name

class Place(models.Model):
  title = models.CharField(max_length=160)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
  slug = models.SlugField(unique=True)
  category = models.ManyToManyField(Category)
  country = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  district = models.CharField(max_length=100)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)
  content = models.TextField()
  image = models.ImageField(upload_to=uploadLocation_placeImage, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
  height_field = models.IntegerField(default=600)
  width_field = models.IntegerField(default=900)
  draft = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  publish = models.DateField(auto_now=False, auto_now_add=False)

  objects = PlaceManager()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("places:place", kwargs={"slug": self.slug})

  class Meta:
    ordering = ["-created", "-updated"]

def create_slug(instance, new_slug=None):
  slug = slugify(instance.title)
  if new_slug is not None:
      slug = new_slug
  qs = Place.objects.filter(slug=slug).order_by("-id")
  exists = qs.exists()
  if exists:
      new_slug = "%s-%s" %(slug, qs.first().id)
      return create_slug(instance, new_slug=new_slug)
  return slug

def pre_save_place_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = create_slug(instance)

pre_save.connect(pre_save_place_receiver, sender=Place) 