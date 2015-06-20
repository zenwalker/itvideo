from videos.models import Video
from django import forms


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ('created_at', 'is_published')
