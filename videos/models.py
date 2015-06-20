from taggit.managers import TaggableManager
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    website = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Video(models.Model):
    title = models.CharField(max_length=255)
    event = models.ForeignKey(Event, blank=True, null=True)
    description = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField()
    tags = TaggableManager(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-year']
