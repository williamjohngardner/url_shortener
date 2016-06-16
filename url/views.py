from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, FormView


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
