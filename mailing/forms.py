from django import forms
from .models import Client, Message, Mailing





class MailingForm(forms.ModelForm):
    clients = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    first_send = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )
    finish_send = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )
    class Meta:
        model = Mailing
        fields = ['message', 'clients', 'first_send', 'finish_send', 'status']
        widgets = {
            'status': forms.Select()
        }