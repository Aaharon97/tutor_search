from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.views import Response
from . import serializers
from django.contrib.auth.models import User
from blog.models import Post, Comment, Category
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model


class CategoryList(APIView):
    def get(self, request):
        all_сategories = Category.objects.all()
        serializer = serializers.CategorySerializer(all_сategories, many=True)

        return Response(serializer.data)

class CategoryDetail(APIView):
    def get(self, request, category_id):
        posts = Post.objects.filter(category__id=category_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostList(APIView):
    def get(self, request):
        all_posts = Post.objects.all()
        serializer = serializers.PostSerializer(all_posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
    def get(self, request, id):
        posts_by_user = Post.objects.filter(user__id=id)
        serializer = serializers.PostSerializer(posts_by_user, many=True)

        return Response(serializer.data)

class CommentList(APIView):
    def get(self, request, id):
        comment_by_post = Comment.objects.filter(post__id=id)
        serializer = serializers.CommentSerializer(comment_by_post, many=True)

        return Response(serializer.data)

class CommentDetail(APIView):
    def get(self, request, id):
        comment_by_user = Comment.objects.filter(user__id=id)
        serializer = serializers.CommentSerializer(comment_by_user, many=True)

        return Response(serializer.data)


class CommentByPost(APIView):

    def get(self, request, id):
        comment_by_post = Comment.objects.filter(post__id=id)
        serializer = serializers.CommentSerializer(comment_by_post, many=True)

        return Response(serializer.data)


class CommentByUser(APIView):

    def get(self, request, id):
        comment_by_user = Comment.objects.filter(user__id=id)
        serializer = serializers.CommentSerializer(comment_by_user, many=True)

        return Response(serializer.data)


class PostsByUser(APIView):

    def get(self, request, id):
        posts_by_user = Post.objects.filter(user__id=id)
        serializer = serializers.PostSerializer(posts_by_user, many=True)

        return Response(serializer.data)


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer = serializers.UserSerializer


    def get(self, request, id):
        profile_by_id = User.objects.filter(user__id=id)
        serializer = serializers.UserSerializer(profile_by_id, many=True)

        return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer