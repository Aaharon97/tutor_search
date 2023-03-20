from django.urls import path, include
from .views import SignUP, UserView, UserProfile, FollowersView, FollowingView, EditUserProfile


urlpatterns = [
    path('SignUp/', SignUP.as_view(), name='accounts-SignUp'),
    path('follow/', UserView.as_view(), name='accounts-follow'),
    path('user/<int:id>/', UserProfile.as_view(), name='accounts-user'),
    path('user/edit/', EditUserProfile.as_view(), name='accounts-user-edit'),
    path('user/<int:id>/followers/', FollowersView.as_view(),
         name='accounts-user-followers'),
    path('user/<int:id>/following/', FollowingView.as_view(),
         name='accounts-user-following'),
]