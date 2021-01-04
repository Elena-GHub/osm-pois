from django.contrib import admin

from .models import Poi
from .models.tag import Tag

admin.site.register(Poi)
admin.site.register(Tag)
