from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from videos.forms import VideoForm
from videos.models import Video


class VideoList(ListView):
    context_object_name = 'videos'
    model = Video


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
