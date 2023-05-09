import datetime
import plotly_express as px
from plotly.offline import plot
from django_pandas.io import read_frame
from django.views.generic import TemplateView, ListView
from django.utils.timezone import make_aware
from .models import RoomEnvironment
from .forms import SearchDataForm
from datetime import timedelta


class CurrentStatusView(TemplateView):
    model = RoomEnvironment
    template_name = 'currentEnvironment.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = RoomEnvironment.objects.latest('measure_time')
        measure_time = queryset.measure_time - timedelta(hours=9)
        measure_time_str = measure_time.strftime("%Y年%m月%d日%H時%M分")
        context['environment'] = queryset
        context['measure_time'] = measure_time_str
        return context


class MonitorStatusView(ListView):
    model = RoomEnvironment
    template_name = 'environmentMonitor.html'

    def get_queryset(self):
        query_set = super().get_queryset()
        self.form = form = SearchDataForm(self.request.GET or None)

        form_start_date = self.request.GET.getlist('start_date')
        form_end_date = self.request.GET.getlist('end_date')
        if (len(form_start_date) == 0) and (len(form_end_date) == 0):
            query_set = query_set.filter(
                measure_time__range=[make_aware(datetime.datetime.now()-timedelta(days=1)-timedelta(hours=9)),
                                    make_aware(datetime.datetime.now()+timedelta(days=1)-timedelta(hours=9))])
            return query_set

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            if start_date and end_date:
                query_set = query_set.filter(measure_time__range=[start_date, end_date])
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        df = read_frame(context['object_list'],
                        fieldnames=['measure_time', 'temperature', 'relative_humidity', 'ambient_light',
                                    'barometric_pressure', 'sound_noise', 'etvoc', 'eco2',
                                    'discomfort_index', 'heat_stroke', 'place'])
        
        df['measure_time'] = df['measure_time'] - timedelta(hours=9)
            
        temperature_plot = px.line(df, x="measure_time", y='temperature', color='place')
        temperature_plot_fig = plot(temperature_plot, output_type='div', include_plotlyjs=False)
        context['temperature_graph'] = temperature_plot_fig

        humidity_plot = px.line(df, x="measure_time", y='relative_humidity', color='place')
        humidity_plot_fig = plot(humidity_plot, output_type='div', include_plotlyjs=False)
        context['humidity_graph'] = humidity_plot_fig

        light_plot = px.line(df, x="measure_time", y='ambient_light', color='place')
        light_plot_fig = plot(light_plot, output_type='div', include_plotlyjs=False)
        context['light_graph'] = light_plot_fig

        pressure_plot = px.line(df, x="measure_time", y='barometric_pressure', color='place')
        pressure_plot_fig = plot(pressure_plot, output_type='div', include_plotlyjs=False)
        context['pressure_graph'] = pressure_plot_fig

        noise_plot = px.line(df, x="measure_time", y='sound_noise', color='place')
        noise_plot_fig = plot(noise_plot, output_type='div', include_plotlyjs=False)
        context['noise_graph'] = noise_plot_fig

        etvoc_plot = px.line(df, x="measure_time", y='etvoc', color='place')
        etvoc_plot_fig = plot(etvoc_plot, output_type='div', include_plotlyjs=False)
        context['etvoc_graph'] = etvoc_plot_fig

        eco2_plot = px.line(df, x="measure_time", y='eco2', color='place')
        eco2_plot_fig = plot(eco2_plot, output_type='div', include_plotlyjs=False)
        context['eco2_graph'] = eco2_plot_fig

        discomfort_plot = px.line(df, x="measure_time", y='discomfort_index', color='place')
        discomfort_plot_fig = plot(discomfort_plot, output_type='div', include_plotlyjs=False)
        context['discomfort_graph'] = discomfort_plot_fig

        heat_stroke_plot = px.line(df, x="measure_time", y='heat_stroke', color='place')
        heat_stroke_plot_fig = plot(heat_stroke_plot, output_type='div', include_plotlyjs=False)
        context['heat_stroke_graph'] = heat_stroke_plot_fig

        return context
