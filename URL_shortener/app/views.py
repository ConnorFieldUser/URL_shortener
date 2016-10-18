from django.shortcuts import render

from django.contrib.auth.models import User

from app.models import Bookmark  # , Profile

from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from django.views.generic import ListView

from django.http import HttpResponseRedirect

# Create your views here.


def index_view(request):
    context = {
    }
    return render(request, 'index.html', context)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class UserListView(ListView):
    template_name = "users.html"
    model = User


class UserDetailView(ListView):
    model = User


def ShortView(View):
    def get(self, request, new_url):
        new = self.kwargs['new_url']
        full = Bookmark.objects.get(neew_url=new)
        return HttpResponseRedirect(full.url)
