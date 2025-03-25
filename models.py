from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)

class Task(models.Model):
    STATUS_CHOICES = [("pending", "Pending"), ("completed", "Completed")]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    users = models.ManyToManyField(User, related_name="tasks")

    def __str__(self):
        return self.name
