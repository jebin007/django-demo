from django.conf.urls import url
from . import views
from django.contrib.auth.views import password_reset
app_name = 'accounts'


urlpatterns = [
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/login
    url(r'^login/$', views.LoginView.as_view(), name='loginu'),

    #music/logout
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    # /music/reset-password/
    url(r'^reset-password/$', password_reset, name='reset-password'),


]