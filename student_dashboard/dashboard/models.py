
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    academic_records = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.student_id})"
