from django.db import models

from client.models import Client
from message.models import Message


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('finished', 'Завершена'),
    ]

    first_send = models.DateTimeField(null=True, blank=True)
    finish_send = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"Рассылка #{self.id} - {self.message.subject}"

class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('success', 'Успешно'),
        ('failed', 'Не успешно'),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='attempts')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=True)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField()

    def __str__(self):
        return f"Попытка рассылки #{self.id} по клиенту {self.client.email} - {self.status} ({self.date_time})"