from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Journey
from datetime import datetime

# Create your views here.


@login_required()
def journeys(request):
    return redirect('app:add')


@login_required()
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        user = request.user

        journey = Journey()
        journey.title = title
        journey.start_date = start_date
        journey.user = user

        journey.save()

        return redirect('home')

    elif request.method == 'GET':
        return render(request, 'add_new_journey.html')
