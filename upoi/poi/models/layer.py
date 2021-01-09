from django.db import models
import poi.models.poi
import poi.models.tag


class Layer(models.Model):
    poi = models.ForeignKey('Poi', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
