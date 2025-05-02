from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    google_profile_picture_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.email
