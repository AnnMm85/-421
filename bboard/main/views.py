from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView

from .forms import RegisterUserForm
from .models import CustUser, Profile, Product


def index(request):
    return render(request, 'main/index.html')


class BBLoginView(LoginView):
    template_name = 'main/login.html'


class RegisterUserView(CreateView):
    model = CustUser
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:login')


def logout_view(request):
    logout(request)

@login_required
def logout_view(request):
    logout(request)
    return redirect('main:index')


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    template_name = 'main/profile.html'


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'main/products.html'
    context_object_name = 'products'
