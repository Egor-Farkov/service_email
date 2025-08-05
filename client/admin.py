from django.contrib import admin

from client.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment', 'count_clients')
    search_fields = ('email', 'full_name')

    @admin.display(description="Символы")
    def count_clients(self, client: Client):
        return f'Кол-во символов в комментарии {len(client.comment)}'