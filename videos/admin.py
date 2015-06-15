from videos.models import Event, Video
from django.contrib import admin


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
