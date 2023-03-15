from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from .models import Comment
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class PostView(TemplateView):
    template_name = 'post.html'

    def get(self, request, id):
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post__id=id)
        params = {
            'post': post,
            'comments': comments
        }
        return render(request, self.template_name, params)


class IndexView(TemplateView):
    template_name = 'main.html'

    @method_decorator(login_required)
    def get(self, request):
        posts = Post.objects.all()[:3]
        followed_users = request.user.profile.first().follows.values_list('id', flat=True) # исправлено
        last_users = User.objects.all().order_by('-id').exclude(id__in=followed_users).exclude(id=request.user.id)[:3]
        params = {
            'posts_recent': posts,
            'last_users': last_users
        }
        return render(request, self.template_name, params)