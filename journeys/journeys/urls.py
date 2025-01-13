from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('accounts/', include('accounts.urls'), name="index"),
    path('', include('app.urls'), name="index"),
]
