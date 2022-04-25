from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from pokemonster.accounts.forms import UserRegisterForm, UserLoginForm
from pokemonster.accounts.models import AppUser, Profile
from pokemonster.fight.models import Fight
from pokemonster.main.models import Customon

UseModel = get_user_model()


class UserRegisterView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'], )
        login(self.request, user)
        return HttpResponseRedirect(reverse('index'))


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')
    form_class = UserLoginForm

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserProfileView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        won_fights = Fight.objects.filter(owner_id=self.request.user.id, win=True)
        lost_fights = Fight .objects.filter(owner_id=self.request.user.id, win=False)
        customons = Customon.objects.filter(owner_id=self.request.user.id)
        context.update({
            'is_owner': self.object.pk == self.request.user.id,
            'won_fights': won_fights,
            'lost_fights': lost_fights,
            'customons': customons
        })

        return context


class UserEditView(views.UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile.html'
    fields = ('name', 'photo', 'gender')

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDeleteView(views.DeleteView):
    model = Profile
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('index')


class LeaderboardView(views.ListView):
    model = Profile
    template_name = 'accounts/leaderboard.html'




