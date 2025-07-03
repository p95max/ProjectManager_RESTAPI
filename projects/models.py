from django.db import models

PROJECT_STATUS_CHOICES = [
    ('active', 'Active'),
    ('archived', 'Archived'),
    ('completed', 'Completed'),
]

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=PROJECT_STATUS_CHOICES, default='active')

    def __str__(self):
        return f'{self.name} - {self.get_status_display()}'

