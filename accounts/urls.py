from django.urls import path, include
from .views import SignUP, ProfileView


urlpatterns = [
    path('SignUp/', SignUP.as_view(), name='accounts-SignUp'),
    path('follow/', ProfileView.as_view(), name='accounts-follow')
]