from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    area = models.CharField(max_length=100, blank=True, null=True)
    can_upload_bills = models.BooleanField(default=True)

class Bill(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20)
    submitted_at = models.DateTimeField(auto_now_add=True)
