from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

TYPE_CHOICES = (
    ('food','FOOD'),
    ('clothes', 'CLOTHES'),
    ('books','BOOKS'),
)

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    resource_type = models.CharField(max_length=7,choices=TYPE_CHOICES,default = 'food')
    def __str__(self):
        return self.content