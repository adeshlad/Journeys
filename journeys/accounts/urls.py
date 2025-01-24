from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', login_required(views.signout), name="signout")
]
