from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
from tinymce.models import HTMLField

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = HTMLField()
    date_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.content