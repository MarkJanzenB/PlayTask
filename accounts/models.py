from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # def create_user(self, email, password=None, **extra_fields):
    #     if not email:
    #         raise ValueError('Users must have an email address')
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)  # Hash password before saving
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = None  # Remove username field if not using it
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    # Add other custom fields as needed (e.g., profile_picture, bio)

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = []  # No additional required fields by default

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # For administrative users
    is_superuser = models.BooleanField(default=False)  # For superuser permissions

    objects = UserManager()

    def __str__(self):
        return self.email
