from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from .views import PostView

urlpatterns = [
    path('posts/<int:id>/', PostView.as_view(), name='blog-post-detail'),
    path('', views.IndexView.as_view(), name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)