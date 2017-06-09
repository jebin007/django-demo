"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    #change the default login url from /accounts/profile/login.html to /music/login.html
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'music/login.html'}, name='login'),


    # /reset-password/done
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    # the name must be equal to password_reset_done

    # /reset-password/confirm
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        name='password_reset_confirm'),
    # the name must be equal to password_reset_confirm

    # /reset-password/complete
    url(r'^reset-password/complete/$', password_reset_complete,
        name='password_reset_complete'),
    # the name must be equal to password_reset_complete


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
