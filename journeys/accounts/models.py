from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    birth_date = models.DateField(editable=True)

    user_name = models.CharField(max_length=255, unique=True)
    profile_photo = models.ImageField(upload_to='users/profile_photos/', blank=True, null=True, default='users/profile_photos/default_profile_photo.jpg')

    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)

    password = models.CharField(max_length=255)


    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
