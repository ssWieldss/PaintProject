from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from paints.forms import ManSignUpForm, ManSignInForm


def index(request):
    return render(request, 'paints/main_page.html')


def main_menu(request):
    return render(request, 'paints/main_menu.html')

def first_paint(request):
    return render(request, 'paints/first_paint.html')


def second_paint(request):
    return render(request, 'paints/second_paint.html')


def outro(request):
    return render(request, 'paints/authors.html')


def main_page(request):
    return render(request, 'paints/main_page.html')


class SignUpView(generic.CreateView):
    form_class = ManSignUpForm
    template_name = 'paints/registration.html'
    success_url = reverse_lazy('main_menu')


class SignInView(LoginView):
    form_class = ManSignInForm
    template_name = 'paints/login.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('main_menu')


def logout_user(request):
    logout(request)
    return redirect('main_page')
