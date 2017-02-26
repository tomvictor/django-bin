from django.db import models
from datetime import datetime
from django.contrib.auth.admin import User
from django.conf import settings

# Create your models here.
VISIBILITY_CHOICES = (
    ('public', 'public'),
    ('private', 'private'),
)


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    status = models.CharField(max_length=100, choices=VISIBILITY_CHOICES,default='public')
    timestamp = models.DateTimeField(default=datetime.now())
    writer = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    hits = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    post = models.ForeignKey(Post,default=1)
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.post)