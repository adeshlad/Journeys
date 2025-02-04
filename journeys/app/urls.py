from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView


app_name = 'app'

urlpatterns = [
    path('', views.journeys, name="journeys"),
    path('add_journey/', views.add_journey, name="add_journey"),
    path('<slug:slug>/', views.view_journey, name="view_journey"),
    path('<slug:slug>/add_location/', views.add_location, name="add_location"),
]
