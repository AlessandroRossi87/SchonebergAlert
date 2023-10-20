from django.urls import path, include
from .blog import views
from .forms import LoginForm
from django.contrib.auth.views import LogoutView
from django.contrib import admin


app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', include('dashboard.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('browse/', views.browse, name='browse'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/category/', views.category, name='category'),
