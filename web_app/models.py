from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    document_type = models.CharField(max_length=100),
    document_number = models.CharField(max_length=100),
    verification_phone_number = models.CharField(max_length=15),
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type} - {self.number} - {self.email} - {self.phone_number} - {'Active' if self.is_active else 'Inactive'}"

class Line(models.Model):
    phone_number = models.CharField(max_length=15),
    lineType = models.CharField(max_length=50),
    operator = models.CharField(max_length=50),
    is_new_line = models.BooleanField(default=False)
    monitored_document = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lines')

class QueryHistory(models.Model):
    lines_found = models.IntegerField(),
    new_lines_found = models.IntegerField(),
    monitored_document = models.ForeignKey(User, on_delete=models.CASCADE, related_name='query_histories')

class Notification(models.Model):
    email = models.EmailField(),
    message = models.TextField(),
    monitored_document = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')