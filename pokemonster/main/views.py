from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from pokemonster.main.forms import AddCustomonForm
from pokemonster.main.models import Customon


class ShowIndex(views.TemplateView):
    template_name = 'main/index.html'


class MyCustomonsView(views.ListView):
    model = Customon
    template_name = 'main/customons.html'


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