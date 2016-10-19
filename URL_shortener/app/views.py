from django.shortcuts import render

from django.contrib.auth.models import User

from app.models import Bookmark  # , Profile

from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from django.views.generic import ListView

from django.http import HttpResponseRedirect

from django.utils.crypto import get_random_string
# get_random_string(length=x)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmark_list"] = Bookmark.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.new_url = ""
        # for i in range(8):

    def ShortView(View):
        def get(self, request, new_url):
            full = Bookmark.objects.get(new_url=new_url)
            return HttpResponseRedirect(full.url)
