from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView


app_name = 'account'

urlpatterns = [
    path('', views.account, name="account"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout")
]
