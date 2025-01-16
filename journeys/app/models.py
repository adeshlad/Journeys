from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Journey(models.Model):
    title = models.CharField(max_length=255, default="Untitled")
    slug = AutoSlugField(populate_from='title', unique=True, default='untitled')

    start_date_time = models.DateTimeField(blank=True, null=True)
    total_days = models.IntegerField(blank=True, null=True)

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='journeys')


class Location(models.Model):
    name = models.CharField(max_length=255, default='Untitled')

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    arrival = models.DateTimeField(blank=True, null=True)
    departure = models.DateTimeField(blank=True, null=True)

    journey = models.ForeignKey('app.Journey', on_delete=models.CASCADE, related_name='locations')


class Location_Photo(models.Model):
    photo = models.ImageField(upload_to='locations/location_photos/', blank=True, null=True, default='locations/location_photos/default_location_photo.jpg')
    caption = models.CharField(max_length=500, blank=True, null=True)

    location = models.ForeignKey("app.Location", on_delete=models.CASCADE, related_name='photos')
