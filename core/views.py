from django.views.generic import TemplateView

from .models import Service, Employee, Feature


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['features'] = Feature.objects.all()
        print(context['features'])
        return context
