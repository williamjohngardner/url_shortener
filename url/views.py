from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, FormView
from url.models import Url


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    success_url = "/"


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


# @login_required
class ProfileView(TemplateView):
    template_name = "profile.html"

    def url_objects(self):
        Url.objects.create()
        data = Url.objects.all()
        return {"data": data}
