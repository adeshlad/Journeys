from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Journey, Location, Location_Photo
from datetime import datetime

# Create your views here.


@login_required()
def journeys(request):
    journeys = Journey.objects.filter(user=request.user)
    return render(request, 'journeys.html', {'journeys': journeys})


@login_required()
def add_journey(request):
    if request.method == 'GET':
        return render(request, 'add_journey.html')

    if request.method == 'POST':
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        user = request.user

        journey = Journey()
        journey.title = title
        journey.start_date = start_date
        journey.user = user
        journey.save()

        return redirect('app:journeys')


@login_required()
def delete_journey(request, journey_slug):
    if request.method == 'POST':
        journey = Journey.objects.get(slug=journey_slug)
        journey.delete()
        return redirect('app:journeys')


@login_required()
def locations(request, journey_slug):
    journey = Journey.objects.get(slug=journey_slug)
    locations = Location.objects.filter(journey=journey)
    return render(request, "locations.html", {'locations': locations,
                                              'journey_slug': journey_slug})


@login_required()
def add_location(request, journey_slug):
    if request.method == 'GET':
        return render(request, "add_location.html", {'journey_slug': journey_slug})

    if request.method == 'POST':
        name = request.POST.get('name')
        arrival = request.POST.get('arrival')
        departure = request.POST.get('departure')
        journey = Journey.objects.get(slug=journey_slug)

        location = Location()
        location.name = name
        location.arrival = arrival
        location.departure = departure
        location.journey = journey
        location.save()

        photos = request.FILES.getlist('location_photos')
        for photo in photos:
            location_photo = Location_Photo()
            location_photo.photo = photo
            location_photo.location = location
            location_photo.save()

        return redirect('app:locations', journey_slug=journey_slug)


@login_required()
def delete_location(request, journey_slug, location_slug):
    if request.method == 'POST':
        journey = Journey.objects.get(slug=journey_slug)
        location = Location.objects.get(slug=location_slug, journey=journey)
        location.delete()
        return redirect('app:locations', journey_slug=journey_slug)


@login_required()
def location_photos(request, journey_slug, location_slug):
    location = Location.objects.get(slug=location_slug)
    photos = Location_Photo.objects.filter(location=location)
    return render(request, "location_photos.html", {'photos': photos,
                                                    'journey_slug': journey_slug,
                                                    'location_slug': location_slug})


@login_required()
def add_location_photos(request, journey_slug, location_slug):
    if request.method == 'GET':
        return render(request, "add_location_photos.html", {'journey_slug': journey_slug,
                                                            'location_slug':location_slug})

    if request.method == 'POST':
        location = Location.objects.get(slug=location_slug)

        photos = request.FILES.getlist('location_photos')
        for photo in photos:
            location_photo = Location_Photo()
            location_photo.photo = photo
            location_photo.location = location
            location_photo.save()

        return redirect('app:location_photos', journey_slug=journey_slug, location_slug=location_slug)


@login_required()
def delete_location_photo(request, journey_slug, location_slug, photo_id):
    if request.method == 'POST':
        journey = Journey.objects.get(slug=journey_slug)
        location = Location.objects.get(slug=location_slug, journey=journey)
        photo = Location_Photo.objects.get(id=photo_id, location=location)
        photo.delete()
        return redirect('app:location_photos', journey_slug=journey_slug, location_slug=location_slug)
