from django.contrib import admin
from .models import Comic, AudioComic, Story

admin.site.register(Comic)
admin.site.register(AudioComic)
admin.site.register(Story)