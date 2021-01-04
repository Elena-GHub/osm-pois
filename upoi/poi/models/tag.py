from django.db import models
# from django.contrib.gis.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
