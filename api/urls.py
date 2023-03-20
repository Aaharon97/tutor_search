from django.urls import path
from .views import CategoryList, CategoryDetail, PostList, PostDetail, CommentList, CommentDetail, \
    PostsByUser, CommentByPost, CommentByUser

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='api-categories'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='api-post-category'),
    path('posts/', PostList.as_view(), name='api-posts'),
    path('posts/user/<int:id>', PostDetail.as_view(), name='api-user-posts'),
    path('comments/post/<int:id>/', CommentList.as_view(), name="api-comment-post"),
    path('comments/user/<int:id>/', CommentDetail.as_view(), name="api-comment-user"),
    path('posts/user/<int:id>/', PostsByUser.as_view(), name='api-user-posts'),
    path('comments/post/<int:id>/', CommentByPost.as_view(), name="api-comment-post"),
    path('comments/user/<int:id>/', CommentByUser.as_view(), name="api-comment-user"),
]