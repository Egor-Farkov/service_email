from django.urls import path

from client.views import ClientList, ClientCreate, ClientUpdate, ClientDelete



urlpatterns = [
    # Клиенты
    path('', ClientList.as_view(), name='clients_list'),
    path('add/', ClientCreate.as_view(), name='client_add'),
    path('<int:pk>/edit/', ClientUpdate.as_view(), name='client_edit'),
    path('<int:pk>/delete/', ClientDelete.as_view(), name='client_delete'),
]