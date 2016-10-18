from django.shortcuts import render

from django.contrib.auth.models import User

from app.models import Bookmark, Profile

from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from django.views.generic import ListView

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
