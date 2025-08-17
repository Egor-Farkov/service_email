from django.urls import path

from message.views import MessageList, MessageCreate, MessageUpdate, MessageDelete

urlpatterns = [

    # Сообщения
    path('', MessageList.as_view(), name='messages_list'),
    path('add/', MessageCreate.as_view(), name='message_add'),
    path('<int:pk>/edit/', MessageUpdate.as_view(), name='message_edit'),
    path('<int:pk>/delete/', MessageDelete.as_view(), name='message_delete'),
]