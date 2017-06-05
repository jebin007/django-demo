from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name ='all_albums'

    def get_queryset(self):
        return Album.objects.all()
    '''by default the variable stored for Album.objects.all() is object_list
    for our index.html to work as {% for album in all_album %} we would have to redefine context_object_name
    to the variable we want.'''

class DetailView(generic.DetailView):
    model=Album
    template_name='music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
class AlbumDelete(DeleteView):
    model = Album
    success_url=reverse_lazy('music:index')