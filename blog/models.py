from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
from tinymce.models import HTMLField
from django import forms
TYPE_CHOICES = (
    ('food','FOOD'),
    ('clothes', 'CLOTHES'),
    ('books','BOOKS'),
)

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    resource_type = models.CharField(max_length=7,choices=TYPE_CHOICES,default = 'food')
    content = HTMLField()
    def __str__(self):
        return self.content