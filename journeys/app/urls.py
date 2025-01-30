from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_new_journey/', views.add_new_journey, name="add_new_journey")
]
