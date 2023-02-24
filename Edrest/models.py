from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Course(models.Model):
    image = models.FileField(upload_to='images/',default=None, null=True, blank=True)
    title = models.CharField(max_length=200, default=None, null=True, blank=True)
    author = models.CharField(max_length=200, default=None, null=True, blank=True)
    rating = models.FloatField()
    price = models.DecimalField(max_digits=6, decimal_places=2,default=None, null=True, blank=True)
    videos = models.ManyToManyField('Video', related_name='courses')

    def __str__(self):
        return self.title
class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/',default=None, null=True, blank=True)

    def __str__(self):
        return self.title
class newuser(AbstractUser):
    username = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='newuser_groups' # new related name
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='newuser_permissions' # new related name
    )