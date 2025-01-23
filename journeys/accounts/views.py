from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_name_exists = User.objects.filter(user_name=user_name).exists()
        email_exists = User.objects.filter(email=email).exists()
        phone_number_exists = User.objects.filter(phone_number=phone_number).exists()
        password_mismatched = password != confirm_password

        if user_name_exists or email_exists or phone_number_exists or password_mismatched:
            next = request.POST.get('next', '/')
            return render(request, 'signup.html', {'next': next,
                                                   'user_name_exists': user_name_exists,
                                                   'email_exists': email_exists,
                                                   'phone_number_exists': phone_number_exists,
                                                   'password_mismatched': password_mismatched})

        user = User()
        user.first_name = first_name
        user.last_name = last_name

        if 'profile_photo' in request.FILES:
            user.profile_photo = request.FILES.get('profile_photo')

        user.user_name = user_name
        user.email = email
        user.phone_number = phone_number
        user.set_password(password)
        user.save()

        login(request, user)

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))

        return redirect('app:index')

    elif request.method == 'GET':
        next = request.GET.get('next', '')
        return render(request, 'signup.html', {'next': next,
                                               'user_name_exists': False,
                                               'email_exists': False,
                                               'phone_number_exists': False,
                                               'password_mismatched': False})


def signin(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(request, user_name=user_name, password=password)
        if user is not None:
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            return redirect('app:index')

        next = request.POST.get('next', '/')
        return render(request, 'signin.html', {'next': next,
                                               'invalid_credentials': True})

    elif request.method == 'GET':
        next = request.GET.get('next', '/')
        return render(request, 'signin.html', {'next': next,
                                               'invalid_credentials': False})


def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:index')
