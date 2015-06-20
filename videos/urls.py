from videos.views import VideoList, VideoDetail, video_add
from django.conf.urls import url

urlpatterns = [
    url(r'^$', VideoList.as_view(), name='video_list'),
    url(r'^add$', video_add, name='video_add'),
    url(r'^(?P<pk>\d+)$', VideoDetail.as_view(), name='video_detail'),
]
