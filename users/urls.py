from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

