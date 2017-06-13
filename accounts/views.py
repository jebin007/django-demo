from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from . forms import UserForm, LoginForm
from django.contrib import messages


class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

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
        return redirect('/accounts/login/')


class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/registration_form.html'

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
