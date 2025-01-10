from django.db import models

# Create your models here.


class Journey(models.Model):
    start_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    total_days = models.IntegerField()


class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    arrival = models.DateTimeField(auto_now=False, auto_now_add=False)
    departure = models.DateTimeField(auto_now=False, auto_now_add=False)
    journey = models.ForeignKey(
        'Journey', on_delete=models.CASCADE, related_name='locations')
