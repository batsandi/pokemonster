from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from pokemonster.accounts.forms import UserRegisterForm, UserLoginForm, UserEditForm
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


class UserProfileView(LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # won_fights = Fight.objects.filter(owner_id=self.object.user_id, win=True)
        # lost_fights = Fight .objects.filter(owner_id=self.object.user.id, win=False)
        customons_count = Customon.objects.filter(owner_id=self.object.user.id).count()
        fights = Fight.objects.filter(owner_id=self.object.user_id).order_by()[::-1][:5]

        context.update({
            'is_owner': self.object.pk == self.request.user.id,
            # 'won_fights': won_fights,
            # 'lost_fights': lost_fights,
            'customons_count': customons_count,
            'fights': fights,

        })

        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = UserEditForm
    template_name = 'accounts/edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def dispatch(self, request,pk, *args, **kwargs):
        user = AppUser.objects.get(id=pk)

        if request.user != user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Profile
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request,pk, *args, **kwargs):
        user = AppUser.objects.get(id=pk)

        if request.user != user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class LeaderboardView(views.ListView):
    model = Profile
    paginate_by = 5
    template_name = 'accounts/leaderboard.html'
