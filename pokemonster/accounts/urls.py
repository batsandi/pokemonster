from django.urls import path

from pokemonster.accounts.views import UserLoginView, UserRegisterView, UserProfileView, UserLogoutView
from pokemonster.accounts.views import LeaderboardView, UserEditView, UserDeleteView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('edit/<int:pk>', UserEditView.as_view(), name='edit profile'),
    path('logout', UserLogoutView.as_view(), name='log out'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete profile'),
    path('leaderboard', LeaderboardView.as_view(), name='leaderboard'),
)
