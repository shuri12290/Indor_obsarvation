from django.shortcuts import render
from django.views.generic import TemplateView


class Experience(TemplateView):
    template_name = 'experience.html'
