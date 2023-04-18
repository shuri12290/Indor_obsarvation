from django.views.generic import TemplateView, ListView
from .models import RoomEnvironment

class CurrentStatusView(TemplateView):
    model = RoomEnvironment
    template_name = 'currentEnvironment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = RoomEnvironment.objects.latest('measure_time')
        context['environment'] = queryset
        return context
    
class MonitorStatusView(ListView):
    model = RoomEnvironment
    template_name = 'environmentMonitor.html'
    