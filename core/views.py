from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from core.forms import ContactForm

from .models import Service, Employee, Feature


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['features'] = Feature.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
