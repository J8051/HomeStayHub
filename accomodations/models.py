from django.db import models

# Create your models here.

class Accomodations(models.Model):
  title = models.CharField(max_length=250)
  type = models.CharField(max_length=250)
  location = models.CharField(max_length=250)
  pricePerNight = models.IntegerField()
  primaryThumbnailImage = models.TextField()
  secondaryImage = models.TextField()
  description = models.TextField()
  maximumGuests = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.IntegerField()
  slug = models.SlugField(unique=True)
  