from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from .models import TutorProfile


class SignUP(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('catalog-index')
        return render(request, self.template_name, {'user_form': user_form})


class ProfileView(RedirectView):

    def post(self, request):
        user = User.objects.get(id=request.POST['user_id'])
        profile = TutorProfile.objects.get(id=request.user.id)
        profile.follows.add(user)

        return redirect('index')