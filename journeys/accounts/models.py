from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(auto_now_add=True)

    user_name = models.CharField(max_length=100, unique=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', default='default_profile_pic.jpg', blank=True, null=True)

    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)

    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
