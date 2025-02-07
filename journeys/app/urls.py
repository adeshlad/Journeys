from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView


app_name = 'app'

urlpatterns = [
    path('', views.journeys, name="journeys"),
    path('add_journey/', views.add_journey, name="add_journey"),
    path('<slug:journey_slug>/delete/', views.delete_journey, name="delete_journey"),

    path('<slug:journey_slug>/', views.locations, name="locations"),
    path('<slug:journey_slug>/add_location/', views.add_location, name="add_location"),
    path('<slug:journey_slug>/locations/<slug:location_slug>/delete/', views.delete_location, name="delete_location"),

    path('<slug:journey_slug>/locations/<slug:location_slug>/', views.location_photos, name="location_photos"),
    path('<slug:journey_slug>/locations/<slug:location_slug>/add_location_photos/', views.add_location_photos, name="add_location_photos"),
    path('<slug:journey_slug>/locations/<slug:location_slug>/location_photos/<int:photo_id>/delete/', views.delete_location_photo, name="delete_location_photo"),
]
