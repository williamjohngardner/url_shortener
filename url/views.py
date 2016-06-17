from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, FormView
from url.models import Url


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["urls"] = Url.objects.all()
        return context


class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    success_url = "/profile"


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class ShortenUrlView(CreateView):
    pass


class CreateBookmarkView(CreateView):
    model = Url
    template_name = "create_bookmark.html"
    fields = ["url", "site_name", "description", "user"]
    success_url = "index.html"

    def form_valid(self, form):
        bookmark = form.save(commit=True)
        bookmark.user = self.request.user
        return super(CreateBookmarkView, self).form_valid(form)


# @login_required
class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    def profile_view(self, request):
        print(request.user)
        user_data = {"data": Url.objects.filter(user=request.user)}
        return render(request, "accounts/profile.html", user_data)

