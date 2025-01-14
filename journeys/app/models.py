from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Journey(models.Model):
    title = models.CharField(max_length=100, default="None")
    slug = AutoSlugField(populate_from='title', unique=True, default='noneclear')

    start_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    total_days = models.IntegerField()


class Location(models.Model):
    name = models.CharField(max_length=100)

    latitude = models.FloatField()
    longitude = models.FloatField()

    arrival = models.DateTimeField(auto_now=False, auto_now_add=False)
    departure = models.DateTimeField(auto_now=False, auto_now_add=False)

    journey = models.ForeignKey(
        'Journey', on_delete=models.CASCADE, related_name='locations')
