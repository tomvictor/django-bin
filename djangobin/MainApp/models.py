from django.db import models
from datetime import datetime
from django.contrib.auth.admin import User
from django.conf import settings

from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.db.models.signals import post_save
from django.dispatch import receiver
from .tom import saltizer


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
    files = models.FileField(blank=True,null=True,upload_to=user_directory_path)
    status = models.CharField(max_length=100, choices=VISIBILITY_CHOICES,default='public')
    timestamp = models.DateTimeField(default=datetime.now())
    writer = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    hits = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, default=None, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        if settings.DEBUG:
            return "http://pasteway.com/%s" % (self.slug)
        return "http://pasteway.com/%s" % (self.slug)


def create_slug(instance, new_slug=None):
    slug = saltizer()
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s%s" %(slug,saltizer())
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender,instance, *args, **kwargs):
    instance.timestamp = datetime.now()
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)