from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Journey
from datetime import datetime

# Create your views here.


@login_required()
def journeys(request):
    journeys = Journey.objects.filter(user=request.user)
    return render(request, 'journeys.html', {'journeys': journeys})


@login_required()
def add_journey(request):
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

    elif request.method == 'GET':
        return render(request, 'add_journey.html')


@login_required
def view_journey(request, slug):
    locations = []
    return render(request, "view_journey.html", {'locations': locations, 'slug': slug})


def add_location(request, slug):
    if request.method == 'POST':
        

        return redirect('app:view_journey', slug=slug)

    elif request.method == 'GET':
        locations = []
        return render(request, "add_location.html", {'locations': locations})
