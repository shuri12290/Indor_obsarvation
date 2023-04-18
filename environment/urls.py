from django.urls import path
from .views import CurrentStatusView, MonitorStatusView

urlpatterns = [
    path('', CurrentStatusView.as_view(), name='currentStatus'),
    path('monitor', MonitorStatusView.as_view(), name='monitor'),
    
]