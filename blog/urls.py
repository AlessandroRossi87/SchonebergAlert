from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', include('post.urls')),
    path('contact/', views.contact, name='contact'),
]
