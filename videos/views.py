from django.views.generic import ListView, DetailView
from videos.models import Video


class VideoList(ListView):
    context_object_name = 'videos'
    model = Video


class VideoDetail(DetailView):
    context_object_name = 'video'
    model = Video

