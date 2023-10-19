from django.contrib import admin
from django.urls import path, include
from blog import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'schonalert'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
