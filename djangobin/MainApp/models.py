from django.db import models
from datetime import datetime
from django.contrib.auth.admin import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
VISIBILITY_CHOICES = (
    ('public', 'public'),
    ('private', 'private'),
)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.writer.username, filename)

class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True,null=True,upload_to=user_directory_path)
    files = models.FileField(blank=True,null=True)
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


