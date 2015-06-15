from videos.views import VideoList, VideoDetail
from django.conf.urls import url

urlpatterns = [
    url(r'^$', VideoList.as_view(), name='video_list'),
    url(r'^(?P<pk>\d+)$', VideoDetail.as_view(), name='video_detail'),
]
