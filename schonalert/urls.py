from django.urls import path, include
from blog import views

app_name = 'schonalert'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/', include('blog.urls')),
]