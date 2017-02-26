from django.db import models

# Create your models here.
VISIBILITY_CHOICES = (
    ('public', 'public'),
    ('private', 'private'),
)


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    status = models.CharField(max_length=100, choices=VISIBILITY_CHOICES,default='public')