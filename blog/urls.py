from django.urls import path, include
from . import views
from post.views import detail
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('posts/', include('post.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
