from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from pokemonster.accounts.models import AppUser
from pokemonster.main.forms import AddCustomonForm, AddCommentForm, EditCustomonForm
from pokemonster.main.models import Customon, Comment


class ShowIndex(views.TemplateView):
    template_name = 'main/index.html'


class MyCustomonsView(LoginRequiredMixin, views.ListView):
    model = Customon
    template_name = 'main/customons.html'

    def get_queryset(self):
        queryset = Customon.objects.filter(owner__user_id=self.request.user.id)
        return queryset


class AddCustomonView(LoginRequiredMixin, views.CreateView):
    template_name = 'main/create_customon.html'
    model = Customon
    form_class = AddCustomonForm
    success_url = reverse_lazy('my customons')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user.profile
        return kwargs


class EditCustomonView(LoginRequiredMixin, views.UpdateView):
    model = Customon
    form_class = EditCustomonForm
    template_name = 'main/edit_customon.html'

    def get_success_url(self):
        return reverse_lazy('my customons')

    def dispatch(self, request,pk, *args, **kwargs):
        customon = Customon.objects.get(pk=pk)
        owner_id = customon.owner.user_id

        if request.user.pk != owner_id:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteCustomonView(LoginRequiredMixin, views.DeleteView):
    model = Customon
    template_name = 'main/delete_cutomon.html'
    success_url = reverse_lazy('my customons')

    def dispatch(self, request,pk, *args, **kwargs):
        customon = Customon.objects.get(pk=pk)
        owner_id = customon.owner.user_id

        if request.user.pk != owner_id:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CustomonWallView(views.ListView):
    model = Customon
    template_name = 'main/customon_wall.html'


class AddCommentView(LoginRequiredMixin, views.CreateView):
    template_name = 'main/create_comment.html'
    model = Comment
    success_url = reverse_lazy('wall')
    form_class = AddCommentForm

    def get_form_kwargs(self):
        customon = Customon.objects.get(
                        pk=self.kwargs['pk'])

        kwargs = super().get_form_kwargs()
        kwargs['customon'] = customon
        kwargs['owner'] = self.request.user.profile
        return kwargs


# blank