from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView
from users.forms import UserRegistrationForm # заменяем импорт на форму из вашего приложения
from django.contrib.auth import authenticate, login
from users.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils import timezone


class SignUP(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_user = authenticate(
                username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            login(request, new_user)
            return redirect('index')
        return render(request, self.template_name, {'user_form': user_form})


class UserView(RedirectView):

    @method_decorator(login_required)
    def post(self, request):
        followed_users = [user for user in request.user.follows.all()]
        user = User.objects.get(id=request.POST['user_id'])
        if user in followed_users:
            request.user.follows.remove(user)
        else:
            request.user.follows.add(user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UserProfile(TemplateView):
    template_name = 'accounts/user_profile.html'

    def get(self, request, id):
        user_profile = User.objects.get(id=id)
        params = {
            'otherUser': user_profile
        }
        return render(request, self.template_name, params)


class EditUserProfile(TemplateView):
    template_name = 'accounts/edit_profile.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        user_form = UserRegistrationForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_user = authenticate(
                username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            login(request, new_user)
            return redirect('index')
        return render(request, self.template_name, {'user_form': user_form})


class FollowersView(TemplateView):
    template_name = "follows.html"

    @method_decorator(login_required)
    def get(self, request, id):
        user = User.objects.get(id=id)
        followers = user.followers.all().exclude(id=user.id)
        user_follows = request.user.follows.all()

        params = {
            'last_users': followers,
            'user_follows': user_follows,
            'title': f"{user.username}'s followers"
        }
        return render(request, self.template_name, params)


class FollowingView(TemplateView):
    template_name = "follows.html"

    @method_decorator(login_required)
    def get(self, request, id):
        user = User.objects.get(id=id)
        follows = user.follows.all().exclude(id=user.id)
        user_follows = request.user.follows.all()

        params = {
            'last_users': follows,
            'user_follows': user_follows,
            'title': f"{user.username}'s following"
        }
        return render(request, self.template_name, params)