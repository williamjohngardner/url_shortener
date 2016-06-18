from hashids import Hashids
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, FormView, DeleteView, UpdateView, ListView
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


class CreateBookmarkView(CreateView):
    model = Url
    template_name = "create_bookmark.html"
    fields = ["url", "site_name", "description"]
    success_url = "/"

    def form_valid(self, form):
        hashids = Hashids(salt="unicornponybagelwhisper")
        bookmark = form.save(commit=False)
        bookmark.hashid = hashids.encode(id(bookmark.url))
        bookmark.user = self.request.user
        return super(CreateBookmarkView, self).form_valid(form)


class DeleteBookmarkView(DeleteView):
    model = Url
    success_url = 'accounts/profile.html'
    template_name = "delete_bookmark.html"
    fields = ["url", "site_name", "description"]


class UpdateBookmarkView(UpdateView):
    model = Url
    success_url = 'accounts/profile.html'
    template_name = "update_bookmark.html"
    fields = ["url", "site_name", "description"]


class ProfileView(ListView):
    template_name = "accounts/profile.html"

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user)

    class Meta:
        ordering = ['-site_name']

    def profile_view(self, request):
        print(request.user)
        user_data = {"data": Url.objects.filter(user=request.user)}
        return render(request, "accounts/profile.html", user_data)

