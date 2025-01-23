from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        birth_date = request.POST['birth_date']

        user_name = request.POST['user_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user_name_exists = User.objects.filter(user_name=user_name).exists()
        email_exists = User.objects.filter(email=email).exists()
        phone_number_exists = User.objects.filter(phone_number=phone_number).exists()
        password_mismatched = password != confirm_password

        if user_name_exists or email_exists or phone_number_exists or password_mismatched:
            return render(request, 'signup.html', {'user_name_exists': user_name_exists,
                                                   'email_exists': email_exists,
                                                   'phone_number_exists': phone_number_exists,
                                                   'password_mismatched': password_mismatched})

        user = User()
        user.first_name = first_name
        user.last_name = last_name

        if birth_date != "":
            user.birth_date = birth_date

        if 'profile_photo' in request.FILES:
            user.profile_photo = request.FILES['profile_photo']
        
        user.user_name = user_name
        user.email = email
        user.phone_number = phone_number
        user.set_password(password)
        user.save()

        login(request, user)

        return redirect('app:index')

    elif request.method == 'GET':
        return render(request, 'signup.html', {'user_name_exists': False,
                                               'email_exists': False,
                                               'phone_number_exists': False,
                                               'password_mismatched': False})


def signin(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(request, user_name=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:index')

        return render(request, 'signin.html', {'invalid_credentials': True})

    elif request.method == 'GET':
        return render(request, 'signin.html', {'invalid_credentials': False})


def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:index')
