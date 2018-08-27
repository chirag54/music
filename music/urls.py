from django.conf.urls import url
from . import views 

app_name = "music"
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.search, name='search'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name="addalbum"),
    url(r'^album/edit/$', views.AlbumUpdate.as_view(), name="Updatealbum"),
    url(r'^song/add/$', views.SongAdd.as_view(), name="addsong"),
]
