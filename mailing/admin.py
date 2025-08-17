
from django.contrib import admin
from .models import Client, Message, Mailing, MailingAttempt





@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'first_send', 'finish_send', 'status')
    list_filter = ('status',)
    filter_horizontal = ('clients',)

@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'date_time', 'status')
    list_filter = ('status',)
    readonly_fields = ('date_time', 'server_response')