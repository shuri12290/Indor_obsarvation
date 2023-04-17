from django.urls import path
from .views import ExperienceView

urlpatterns = [
    path('', ExperienceView.as_view(), name='experience'),
]