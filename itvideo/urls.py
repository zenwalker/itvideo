from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from pages import views as pages

urlpatterns = [
    url(r'^django/', include(admin.site.urls)),
    url(r'^videos/', include('videos.urls')),
    url(r'^$', pages.page_home, name='home'),
]
