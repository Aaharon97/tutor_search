from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    city = forms.CharField(required=False)
    country = forms.CharField(required=False)
    bio = forms.CharField(required=False)
    inst_username = forms.CharField(required=False)
    tg_username = forms.CharField(required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'city',
                  'country', 'bio', 'inst_username', 'tg_username', 'photo')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords didn't match!")
        return data['password2']