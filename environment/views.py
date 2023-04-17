from django.views.generic import TemplateView, ListView
from .models import RoomEnvironment

class CurrentStatusView(TemplateView):
    model = RoomEnvironment
    
    
class MonitorStatusView(ListView):
    model = RoomEnvironment