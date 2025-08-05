from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from client.forms import ClientForm
from client.models import Client


class ClientList(ListView):
    model = Client
    template_name = 'clients_list.html'
    context_object_name = 'clients'

class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('clients_list')

class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('clients_list')

class ClientDelete(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('clients_list')