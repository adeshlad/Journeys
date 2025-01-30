from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required()
def index(request):
    return render(request, 'index.html')


# @login_required()
def add_new_journey(request):
    return render(request, 'add_new_journey.html')