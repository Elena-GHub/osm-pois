from django.db import models
import poi.models.poi
import poi.models.layer


class Tag(models.Model):
    name = models.CharField(max_length=100)
    pois = models.ManyToManyField('Poi', through='Layer')


    def __str__(self):
        return self.name
