from django.urls import path

from . import views
from .views import*

urlpatterns = [
    path('registration', views.SignUpView.as_view(), name='registration'),
    path('login', views.SignInView.as_view(), name='login'),
    path('main_menu', views.main_menu, name='main_menu'),
    path('first_paint', views.first_paint, name='first_paint'),
    path('second_paint', views.second_paint, name='second_paint'),
    path('authors', views.outro, name='authors'),
    path('', views.main_page, name='main_page'),
    path('logout', views.logout_user, name='logout'),
]