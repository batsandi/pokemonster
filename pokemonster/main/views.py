from django.shortcuts import render
from django.views import generic as views


class ShowIndex(views.TemplateView):
    template_name = 'main/index.html'
