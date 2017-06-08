from django.views import generic
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
    template_name='music/index.html'
    context_object_name ='all_albums'

    def get_queryset(self):
        return Album.objects.all()
    '''by default the variable stored for Album.objects.all() is object_list
    for our index.html to work as {% for album in all_album %} we would have to redefine context_object_name
    to the variable we want.'''
@method_decorator(login_required, name='dispatch')
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
class SongCreate(CreateView):
    model = Song
    fields = ['file_type','album','song_title', 'song_file']

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form': form})
    #process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False) #this saves the form locally but not into the database for further validation
            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save() #this saves the user to the database.

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)     #log the user in and attach a session
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form})

class LoginView(View):
    form_class = LoginForm
    template_name = 'music/login.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process form data
    def post(self,request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)  # log the user in and attach a session
            return redirect('music:index')

        error_message = "Invalid Login Credentials" #this is how you raise error when invalid login with render
        return render(request, self.template_name, {'form': form, 'error_message': error_message})

class LogoutView(View):
    form_class = LoginForm
    def get(self, request):
        logout(request)
        # if all goes well
        messages.add_message(request, messages.INFO, 'You are now logged out successfully!!')
        return redirect('/music/login/')




