from django.urls import path

from pokemonster.accounts.views import UserLoginView, UserRegisterView, UserProfileView
from pokemonster.accounts.views import    UserListView, UserEditView, UserDeleteView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('leaderboard', UserListView.as_view(), name='leaderboard'),
    path('edit/<int:pk>', UserEditView.as_view(), name='edit profile'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete profile')

)
