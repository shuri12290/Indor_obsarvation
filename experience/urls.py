from django.urls import path
from .views import Experience

urlpatterns = [
    path('', Experience.as_view()),
]