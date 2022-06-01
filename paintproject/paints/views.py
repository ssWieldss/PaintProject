from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from paints.forms import ManSignUpForm, ManSignInForm
from paints.models import Paint


def index(request):
    return render(request, 'paints/main_page.html')


def main_menu(request):
    return render(request, 'paints/main_menu.html')


def first_paint(request):
    return render(request, 'paints/paint_page.html')


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


def paints_all_view(request):
    paints = Paint.objects.all()
    context = {'paints': paints}
    return render(request, 'paints/main_menu.html', context=context)


class PaintView(generic.DetailView):
    model = Paint
    template_name = "paints/paint_page.html"
    context_object_name = "paint"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        try:
            context["next"] = Paint.objects.get(pk=(self.object.pk + 1))
        except Paint.DoesNotExist:
            pass

        try:
            context["previous"] = Paint.objects.get(pk=(self.object.pk - 1))
        except Paint.DoesNotExist:
            pass
        return self.render_to_response(context)
