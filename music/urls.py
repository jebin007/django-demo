from django.conf.urls import url
from . import views
app_name = 'music'
urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/song/add
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/2/song-delete
    url(r'(?P<pk>[0-9]+)/song/delete/$', views.SongDelete.as_view(), name='song-delete'),

    #/music/login
    url(r'^login/$', views.LoginView.as_view(), name='loginu'),

    #music/logout
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]