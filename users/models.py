from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length = 10)
    address = models.CharField(max_length = 256)

    def __str__(self):
        return self.email