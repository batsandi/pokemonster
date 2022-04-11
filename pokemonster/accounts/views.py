from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from pokemonster.accounts.forms import UserRegisterForm
from pokemonster.accounts.models import AppUser, Profile


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserRegisterView(views.CreateView):
    template_name = 'accounts/register.html'
    model = AppUser
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')


class UserProfileView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'is_owner': self.object.pk == self.request.user.id
        })

        return context


class UserEditView(views.UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile.html'
    fields = ('name', 'photo', 'gender')

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DeleteView):
    model = Profile
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('index')


class UserListView(views.ListView):
    model = Profile
    template_name = 'accounts/leaderboard.html'

