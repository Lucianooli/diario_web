from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topic/<topic_id>/', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_topic/<topic_id>', views.delete_topic, name='delete_topic'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
