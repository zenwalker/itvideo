from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from videos.forms import VideoForm
from videos.models import Video


class VideoList(ListView):
    context_object_name = 'videos'
    model = Video

    def get_queryset(self):
        videos = super().get_queryset()
        tags = self.request.GET.get('tags')

        if not tags:
            return videos

        return videos.filter(tags__slug__in=tags.split(','))


class VideoDetail(DetailView):
    context_object_name = 'video'
    model = Video


def video_add(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():
            video = form.save()
            data = {'video': video, 'form': VideoForm()}
            return render('videos/video_add_success.html', data)

    data = {'form': VideoForm()}
    return render(request, 'videos/video_add.html')
