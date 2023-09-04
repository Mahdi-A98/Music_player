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


class Login(FormView):
    form_class = UserLoginForm
    template_name = 'account/login_page.html'
    success_url = reverse_lazy('music:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("it's login")
            return redirect(reverse_lazy('music:home'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        cd = form.cleaned_data.copy()
        user = authenticate(self.request, username=cd['username'], password=cd['password'])
        if User.objects.filter(Q(email=cd['username'])|Q(username=cd['username'])):
            if user:
                print('user exist')
                login(self.request, user, 'account.authentication.MyUserBackend')
                print('login view: user is logged in')
                # message = f"Hey {user.get_full_name()}/n/t you registered in MusiTo successfully."
                # user.email_user("Registered successfully", message)
                return super().form_valid(form)
            form.add_error("password", "Incorrect Password! ")
            return super().form_invalid(form)
        form.add_error("username", "Username or Email not found! ")
        return super().form_invalid(form)


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('account:login'))