from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout

from account.authentication import MyUserBackend
from account.models import User
from .forms import CreatePlayListForm


from .models import Song, PlayList, Gener
# Create your views here.
class Home(ListView):
    model = Song
    template_name = 'music/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = PlayList.objects.filter(owner=self.request.user) if isinstance(self.request.user, User) else []
        context["playlist_form"] = CreatePlayListForm()
        return context
    

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         print('home view: user is logged in')
    #     else:
    #         print('home view: user is  not logged in')

    #     # print(self.request.user)
    #     # print(type(self.request.user))
    #     return super().dispatch(request, *args, **kwargs)
    