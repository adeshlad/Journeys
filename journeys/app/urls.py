from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView


app_name = 'app'

urlpatterns = [
    path('', views.journeys, name="journeys"),
    path('add_journey/', views.add_journey, name="add_journey"),
    path('<slug:slug>/', views.journeys, name="view_journey"),
]
