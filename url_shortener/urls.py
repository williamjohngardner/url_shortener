"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from url.views import IndexView, CreateUserView, CreateBookmarkView, ProfileView, DeleteBookmarkView, UpdateBookmarkView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^create_user/$', CreateUserView.as_view(), name="create_user"),
    url(r'^login/$', login, name="login"),
    url(r'^accounts/profile/$', login_required(ProfileView.as_view()), name="profile"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^create_bookmark/$', CreateBookmarkView.as_view(), name="create_bookmark"),
    url(r'^delete_bookmark/(?P<pk>\d+)$', DeleteBookmarkView.as_view(), name="delete_bookmark"),
    url(r'^update_bookmark/(?P<pk>\d+)$', UpdateBookmarkView.as_view(), name="update_bookmark")

]
