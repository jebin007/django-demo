from django.views import generic
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import UserForm, LoginForm
from .models import Album, Song
from django.contrib import messages


class IndexView(generic.ListView):
    template_name= 'music/index.html'
    context_object_name ='all_albums'

    def get_queryset(self):
        return Album.objects.all()
    '''by default the variable stored for Album.objects.all() is object_list
    for our index.html to work as {% for album in all_album %} we would have to redefine context_object_name
    to the variable we want.'''

@require_http_methods(["GET"])
@login_required
def album_detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    context = {'album': album}
    return render(request, 'music/detail.html', context=context)

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']



class AlbumDelete(DeleteView):
    model = Album
    success_url=reverse_lazy('music:index')


class SongCreate(CreateView):
    model = Song
    fields = ['file_type','album','song_title', 'song_file']


@require_http_methods(["GET", "POST"])
@login_required
def delete_song(request, pk):
    song = Song.objects.get(pk=pk)
    if song is None:
        redirect('/music/')

    album_id = song.album_id
    status = song.delete()
    response = redirect(f"/music/detail/{album_id}")
    # response['Location'] += album_id
    return response








