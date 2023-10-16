from django.urls import path, include
from . import views
from post.views import detail

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('posts/', include('post.urls')),
]