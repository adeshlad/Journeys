from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Journey(models.Model):
    title = models.CharField(max_length=255, default="Untitled")
    slug = AutoSlugField(populate_from='title', unique=True)

    start_date = models.DateField()
    total_days = models.IntegerField(blank=True, null=True)

    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='journeys')


class Location(models.Model):
    name = models.CharField(max_length=255, default='Untitled')
    slug = AutoSlugField(populate_from='name', unique=True)

    arrival = models.DateTimeField(blank=True, null=True)
    departure = models.DateTimeField(blank=True, null=True)

    journey = models.ForeignKey('app.Journey', on_delete=models.CASCADE, related_name='locations')


class Location_Photo(models.Model):
    photo = models.ImageField(upload_to='locations/location_photos/')

    location = models.ForeignKey("app.Location", on_delete=models.CASCADE, related_name='photos')
