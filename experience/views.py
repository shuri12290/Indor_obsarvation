from django.shortcuts import render
from django.views.generic import TemplateView


class ExperienceView(TemplateView):
    template_name = 'experience.html'
