from django.urls import path

from . import views
from .views import*

urlpatterns = [
    path('registration', views.SignUpView.as_view(), name='registration'),
    path('login', views.SignInView.as_view(), name='login'),
    path('main_menu', views.paints_all_view, name='main_menu'),
    path('first_paint', views.first_paint, name='first_paint'),
    path('second_paint', views.second_paint, name='second_paint'),
    path('authors', views.outro, name='authors'),
    path('', views.main_page, name='main_page'),
    path('logout', views.logout_user, name='logout'),
    path('paint/<int:pk>/', views.PaintView.as_view(), name="paint_page"),
    path('like/', views.like, name='like'),
    path('get_likes_count/<int:pk>/', views.get_likes_count, name='get_likes_count')
]
