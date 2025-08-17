from django.urls import path

from mailing import views

urlpatterns = [

    # Рассылки
    path('', views.MailingList.as_view(), name='mailings_list'),
    path('add/', views.MailingCreate.as_view(), name='mailing_add'),
    path('<int:pk>/edit/', views.MailingUpdate.as_view(), name='mailing_edit'),
    path('<int:pk>/delete/', views.MailingDelete.as_view(), name='mailing_delete'),
    path('<int:mailing_id>/attempts/', views.MailingAttemptList.as_view(), name='mailing_attempts_list'),

    # Отправка рассылки вручную
    path('<int:pk>/send/', views.send_mailing, name='mailing_send'),
]