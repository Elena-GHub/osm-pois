from django.db import models
from .tag import Tag
from .layer import Layer


class Poi(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=150)
    # coordinates = models.PointField()
    coordinates = models.CharField(max_length=100)
    social_media = models.CharField(max_length=300)
    tags = models.ManyToManyField('Tag', through='Layer')


    def __str__(self):
        return self.name
