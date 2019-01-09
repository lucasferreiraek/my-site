from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    ref = models.CharField(max_length=4)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50)


    def __str__(self):
        return self.title
