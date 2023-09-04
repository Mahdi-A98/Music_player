from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView , ListView, DetailView, FormView
from django.db.models import Q

from .authentication import MyUserBackend
from .models import User
from .forms import UserRegisterForm, UserLoginForm

class Register(CreateView):
    form_class = UserRegisterForm
    template_name = 'account/sign_up_page.html'
    success_url = reverse_lazy('music:home')

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return redirect(reverse_lazy('music:home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        print('self.request: ', self.request)
        if user:
            print('user exist')
            login(self.request, user, 'account.authentication.MyUserBackend')
            if user.is_authenticated:
                print('register view: user is logged in')
            else:
                print('register view: user is not logged in')
        # message = f"Hey {user.get_full_name()}/n/t you registered in MusiTo successfully."
        # user.email_user("Registered successfully", message)
        return redirect(reverse_lazy('music:home'))
