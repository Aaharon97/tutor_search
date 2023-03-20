from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import PostView, SearchView, FeedView, CommentView, CreateCommentView, IndexView, PostDeleteView


urlpatterns = [
    path('posts/<int:id>/', PostView.as_view(), name='blog-post-detail'),
    path('posts/create/', PostView.as_view(), name='blog-post-create'),
    path('posts/<int:pk>/delete/',
         PostDeleteView.as_view(), name='blog-post-delete'),
    path('posts/comment/create/', CreateCommentView.as_view(),
         name='blog-post-comment-create'),
    path('posts/comment/delete/', CommentView.as_view(),
         name='blog-post-comment-delete'),
    path('', IndexView.as_view(), name="index"),
    path('blog/search/', SearchView.as_view(), name='blog-search'),
    path('feed/', FeedView.as_view(), name='blog-feed'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)