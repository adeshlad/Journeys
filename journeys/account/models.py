from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, user_name, password, **extra_fields):
        if not user_name or not password:
            raise ValueError("The user_name field must be set")

        user = self.model(user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    profile_photo = models.ImageField(upload_to='users/profile_photos/', blank=True, null=True)

    # GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    # birth_date = models.DateField(blank=True, null=True)

    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']

    def __str__(self):
        return self.user_name
