from taggit.managers import TaggableManager
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    descriptiom = models.TextField(blank=True)
    website = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Video(models.Model):
    title = models.CharField(max_length=255)
    event = models.ForeignKey(Event, blank=True, null=True)
    date = models.DateField()
    tags = TaggableManager()
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
