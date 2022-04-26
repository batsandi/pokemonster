from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from pokemonster.main.forms import AddCustomonForm, AddCommentForm
from pokemonster.main.models import Customon, Comment


class ShowIndex(views.TemplateView):
    template_name = 'main/index.html'


class MyCustomonsView(views.ListView):
    model = Customon
    template_name = 'main/customons.html'

    def get_queryset(self):
        queryset = Customon.objects.filter(owner__user_id=self.request.user.id)
        return queryset

class AddCustomonView(views.CreateView):
    template_name = 'main/create_customon.html'
    model = Customon
    form_class = AddCustomonForm
    success_url = reverse_lazy('my customons')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user.profile
        return kwargs


class CustomonWallView(views.ListView):
    model = Customon
    template_name = 'main/customon_wall.html'


class AddCommentView(views.CreateView):
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

