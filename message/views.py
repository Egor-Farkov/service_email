from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from message.forms import MessageForm
from message.models import Message


# Create your views here.

class MessageList(ListView):
    model = Message
    template_name = 'messages_list.html'
    context_object_name = 'messages'

class MessageCreate(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('messages_list')

class MessageUpdate(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('messages_list')

class MessageDelete(DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('messages_list')